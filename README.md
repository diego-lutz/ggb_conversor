# Conversor de GeoGebra para PyOpenGL

Este projeto foi criado para facilitar a criação de desenhos 2D em PyOpenGL, especialmente para trabalhos de faculdade e projetos pessoais. A ferramenta principal converte um arquivo `.ggb` do GeoGebra em tuplas de Python (`vértices` e `arestas`), eliminando a necessidade de digitar coordenadas manualmente.

## O que o projeto faz?

-   **`ggb.py`**: Uma aplicação com interface gráfica (GUI) que lê um arquivo `.ggb`, extrai os pontos e segmentos, e gera o código formatado para as variáveis `vertice` e `aresta`.
-   **`main.py`**: Um script básico de PyOpenGL que usa as variáveis `vertice` e `aresta` para renderizar o seu desenho em uma janela.

## Requisitos

-   Python 3.x
-   PyCharm (ou qualquer outro editor de código Python)
-   Bibliotecas: `PyOpenGL` e `pygame`

---

## Tutorial Completo: Do Desenho à Renderização

Siga estes passos para transformar sua imagem em um objeto 2D no PyOpenGL.

### Parte 1: Criando seu Desenho no GeoGebra

O primeiro passo é vetorizar sua imagem, ou seja, desenhar os segmentos que formam a sua figura.

1.  **Abra o GeoGebra Clássico** (pode ser o online ou o aplicativo para desktop).
2.  **Adicione uma imagem de fundo** para servir como guia.
    -   No menu, vá em `Editar` -> `Inserir Imagem de` -> `Arquivo` e selecione sua imagem.
3.  **Desenhe sobre a imagem** usando a ferramenta **Segmento**.
    -   Selecione a ferramenta `Segmento` na barra de ferramentas.
    -   Clique nos pontos-chave da sua imagem para criar as linhas (arestas) do seu desenho. Tente ser preciso, pois cada clique criará um vértice.
4.  **Salve o arquivo**.
    -   Quando terminar de desenhar, vá em `Arquivo` -> `Baixar como...` -> `Arquivo GeoGebra (.ggb)`.
    -   Salve o arquivo em um local de fácil acesso no seu computador.

### Parte 2: Configurando o Projeto no PyCharm

Agora, vamos preparar o ambiente para usar os scripts Python.

1.  **Baixe o Código do GitHub.**
    -   Clique no botão verde `<> Code` -> `Download ZIP`.
    -   Extraia a pasta para o local de sua preferência.

2.  **Abra o Projeto no PyCharm.**
    -   Abra o PyCharm e vá em `File` -> `Open...` e selecione a pasta que você acabou de extrair.

### Parte 3: Convertendo o Arquivo `.ggb`

É hora de usar o conversor para gerar nosso código.

1.  **Execute o `ggb.py`**.
    -   No PyCharm, encontre o arquivo `ggb.py` na lista de arquivos, clique com o botão direito sobre ele e selecione `Run 'ggb'`.

2.  **Selecione seu arquivo `.ggb`**.
    -   Na janela que abrir, clique no botão **"1. Selecionar Arquivo .ggb e Converter"**.
    -   Navegue até o local onde você salvou seu arquivo `.ggb` e abra-o.

3.  **Copie o Resultado**.
    -   O código formatado para os vértices e arestas aparecerá na caixa de texto.
    -   Clique no botão **"2. Copiar Resultado"** para copiar todo o conteúdo para a área de transferência.

### Parte 4: Atualizando o Código do PyOpenGL

Vamos inserir o código gerado no script principal.

1.  **Abra o arquivo `main.py`** no PyCharm.
2.  **Localize as variáveis** `vertice` e `aresta` no início do arquivo. Elas terão um conteúdo de exemplo.
3.  **Substitua TUDO**. Selecione o bloco inteiro da variável `vertice` (de `vertice = (` até o `)`) e o bloco inteiro da variável `aresta` e apague-os.
4.  **Cole o código** que você copiou do conversor. O seu código agora deve ter as novas variáveis.

**Exemplo de como o código deve ficar depois de colar:**
```python
# Conteúdo colado do conversor.
# Ele já contém as duas variáveis formatadas.

vertice = (
    (10.5, -5.2),
    (-8.1, 4.3),
    # ... Seus novos dados ...
)

aresta = (
    (0, 1),
    # ... Suas novas arestas ...
)

## Parte 5: Instalando as Dependências e Executando

O último passo é instalar as bibliotecas necessárias e ver a mágica acontecer.

1. Abra o **Terminal** no PyCharm.  
2. Na parte inferior do PyCharm, clique na aba **Terminal**.  
3. Instale as bibliotecas. Digite os seguintes comandos, um de cada vez, e pressione **Enter**:

```bash
pip install PyOpenGL
pip install pygame

