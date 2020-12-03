from OpenGL.GL import *
from OpenGL.GLU import *


def wii_character(wiiX, wiiY, wiiZ):
    glRotatef(90, 1, 0, 0)
    glTranslate(wiiX, wiiY, wiiZ)
    body()
    head()


def head():
    glPushMatrix()
    glColor3f(.5, .35, .05)
    glTranslatef(0, 0, -.4)
    cyl = gluNewQuadric()
    gluSphere(cyl, .7, 100, 10)
    glPopMatrix()


def body():
    glPushMatrix()
    glColor3f(1, 1, 0)
    quadratic = gluNewQuadric()
    gluCylinder(quadratic, .5, 1, 2, 100, 10)
    glPopMatrix()
