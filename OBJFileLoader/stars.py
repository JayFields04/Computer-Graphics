# Stars
import random
from OpenGL.GL import *


def rand_coord():
    listx = []
    listy = []
    for i in range(0, 50):
        r = random.randint(-100, 100)
        listx.append(r)
        j = random.randint(-100, 100)
        listy.append(j)
    return listx, listy


def stars(x_pos, y_pos):
    glLoadIdentity()
    glColor3f(1, 1, 1)
    z = -80
    glBegin(GL_LINE_LOOP)
    glVertex3f(0.0 + x_pos, 0.2 + y_pos, z)
    glVertex3f(0.1 + x_pos, 0.1 + y_pos, z)
    glVertex3f(0.2 + x_pos, 0.05 + y_pos, z)
    glVertex3f(0.1 + x_pos, 0.0 + y_pos, z)
    glVertex3f(0.2 + x_pos, -0.1 + y_pos, z)
    glVertex3f(0.0 + x_pos, 0.0 + y_pos, z)
    glVertex3f(-0.2 + x_pos, -0.1 + y_pos, z)
    glVertex3f(-0.1 + x_pos, 0.0 + y_pos, z)
    glVertex3f(-0.2 + x_pos, 0.05 + y_pos, z)
    glVertex3f(-0.1 + x_pos, 0.1 + y_pos, z)
    # glTranslatef(-90, 100, -250)
    glEnd()
