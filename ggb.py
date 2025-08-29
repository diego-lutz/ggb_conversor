import tkinter as tk
from tkinter import filedialog, scrolledtext
import zipfile
import xml.etree.ElementTree as ET
import os
import itertools


def converter_com_logica_matematica(caminho_arquivo):
    """
    Converte o arquivo .ggb usando lógica matemática para reconstruir as arestas
    quando as conexões explícitas não estão presentes.
    """
    if not caminho_arquivo:
        return "Nenhum arquivo selecionado."

    try:
        with zipfile.ZipFile(caminho_arquivo, 'r') as ggb_zip:
            if 'geogebra.xml' not in ggb_zip.namelist():
                return "Erro: Arquivo 'geogebra.xml' não encontrado."

            with ggb_zip.open('geogebra.xml') as xml_file:
                tree = ET.parse(xml_file)
                root = tree.getroot()
                construction = root.find('construction')

                if construction is None:
                    return "Erro: Tag <construction> não encontrada."

                pontos = []
                segmentos = []

                # --- PASSO 1: Coletar todos os pontos e segmentos separadamente ---
                for element in construction.findall('element'):
                    tipo = element.get('type')
                    label = element.get('label')
                    coords_tag = element.find('coords')

                    if tipo == 'point' and coords_tag is not None:
                        try:
                            x = float(coords_tag.get('x'))
                            y = float(coords_tag.get('y'))
                            pontos.append({'label': label, 'coords': (x, y)})
                        except (ValueError, TypeError):
                            continue

                    elif tipo == 'segment' and coords_tag is not None:
                        try:
                            a = float(coords_tag.get('x'))
                            b = float(coords_tag.get('y'))
                            c = float(coords_tag.get('z'))
                            segmentos.append({'label': label, 'equation': (a, b, c)})
                        except (ValueError, TypeError):
                            continue

                if not pontos:
                    return "Nenhum ponto válido encontrado no arquivo."

                # --- PASSO 2: Reconstruir as arestas com lógica matemática ---
                arestas_encontradas = []
                TOLERANCIA = 1e-9
                mapa_indices = {p['label']: i for i, p in enumerate(pontos)}

                for seg in segmentos:
                    pontos_na_reta = []
                    a, b, c = seg['equation']

                    for i, ponto in enumerate(pontos):
                        px, py = ponto['coords']
                        if abs(a * px + b * py + c) < TOLERANCIA:
                            pontos_na_reta.append(mapa_indices[ponto['label']])

                    if len(pontos_na_reta) >= 2:
                        for par in itertools.combinations(pontos_na_reta, 2):
                            if tuple(sorted(par)) not in [tuple(sorted(a)) for a in arestas_encontradas]:
                                arestas_encontradas.append(par)

                # --- PASSO 3: Formatar a string de saída ---
                output_string = "vertice = (\n"
                for p in pontos:
                    # Alteração: Comentários removidos daqui
                    output_string += f"    {p['coords']},\n"
                output_string += ")\n\n"

                output_string += "aresta = (\n"
                for a in arestas_encontradas:
                    output_string += f"    {a},\n"
                output_string += ")\n"

                return output_string

    except Exception as e:
        return f"Ocorreu um erro ao processar o arquivo:\n{e}"


def selecionar_arquivo_e_converter():
    tipos_de_arquivo = (("Arquivos GeoGebra", "*.ggb"), ("Todos os arquivos", "*.*"))
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo GeoGebra para converter",
        filetypes=tipos_de_arquivo
    )
    if caminho_arquivo:
        caminho_var.set(f"Arquivo: {os.path.basename(caminho_arquivo)}")
        texto_resultado.delete('1.0', tk.END)
        resultado = converter_com_logica_matematica(caminho_arquivo)
        texto_resultado.insert(tk.END, resultado)


# --- NOVA FUNÇÃO PARA O BOTÃO DE COPIAR ---
def copiar_resultado():
    # Pega todo o texto do widget de resultado
    conteudo = texto_resultado.get('1.0', tk.END)
    if conteudo.strip():  # Só copia se não estiver vazio
        # Limpa a área de transferência e adiciona o novo conteúdo
        root.clipboard_clear()
        root.clipboard_append(conteudo)

        # Fornece feedback visual ao usuário
        texto_original = btn_copiar.cget("text")
        btn_copiar.config(text="Copiado!", state="disabled")
        root.after(2000, lambda: btn_copiar.config(text=texto_original, state="normal"))


# --- Interface Gráfica (com o novo botão) ---
root = tk.Tk()
root.title("Conversor GeoGebra (com Lógica Matemática)")
root.geometry("700x550")
root.minsize(500, 400)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(expand=True, fill='both')

# Frame para os botões
frame_botoes = tk.Frame(frame)
frame_botoes.pack(fill='x', pady=(0, 10))

btn_selecionar = tk.Button(frame_botoes, text="1. Selecionar Arquivo .ggb e Converter",
                           command=selecionar_arquivo_e_converter)
btn_selecionar.pack(side='left', expand=True, fill='x', padx=(0, 5))

# --- NOVO BOTÃO DE COPIAR ---
btn_copiar = tk.Button(frame_botoes, text="2. Copiar Resultado", command=copiar_resultado)
btn_copiar.pack(side='left', expand=True, fill='x', padx=(5, 0))

caminho_var = tk.StringVar(value="Nenhum arquivo selecionado.")
lbl_caminho = tk.Label(frame, textvariable=caminho_var)
lbl_caminho.pack(pady=(0, 10))

lbl_info = tk.Label(frame, text="O código formatado para PyOpenGL aparecerá abaixo:")
lbl_info.pack()

texto_resultado = scrolledtext.ScrolledText(frame, wrap=tk.WORD)
texto_resultado.pack(expand=True, fill='both', pady=(5, 0))

root.mainloop()
