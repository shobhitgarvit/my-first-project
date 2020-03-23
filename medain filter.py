import numpy as np
import cv2

from matplotlib import pyplot as plt
random_matrix_array = np.random.randint(1, 1550, size=(6, 4))
median = cv2.medianBlur(random_matrix_array,3)


plt.imshow(median)
plt.show()
print('random matrix = ',random_matrix_array)
print('---------------------------------------------------------------------------------------------/n')
print('after using filtering the pixel size is nearly same /n')
print(median)

#-----------------------------------------------------------------------------------------------------------------
#rotaing plane code

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (1, 1, 1),
    (1, -1, 1),
    (0,0,0)
    )

edges = (
    (0,1),
    (0,3),
    (2,1),
    (2,3),
    (4,0),
    (4, 1),
    (4, 2),
    (4, 3)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()
