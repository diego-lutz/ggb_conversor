import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertice = (

)
aresta = (

)

def Quadrado():
    glBegin(GL_LINES)
    for temp_aresta in aresta:
        for vertex in temp_aresta:
            glVertex2f(*vertice[vertex])  # Aceita coordenadas float
    glEnd()



def main():
    pygame.init() #Inicialize todos os módulos pygame importados
    display = (1080, 720) #Define o tamanho da tela (Plano)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL) #insere o código do pygame dentro do display de demonstração
    gluPerspective(80, #quantos graus o objeto será posicinado
                   (display[0]/display[1]), #tamanho da dela, no caso 700x700,
                   1, #o qual distante o objeto será renderizado
                   20 #Distância a ser desenhado.
    )

    glTranslatef(
        0, #X
        0, #Y
        -5 #Z
    )

    glRotatef(45,  # angulo de retação
              0,  # x
              0,  # y
              0  # z
              )  # Transformação geometrica de rotação



    glColor3f(1,1,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Quadrado()
        pygame.display.flip()
        #pygame.time.wait(10)


main()
