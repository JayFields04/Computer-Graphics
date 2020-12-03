import math
from OpenGL.GL import *
from OpenGL.GLU import *


def basketball_hoop():
    rim()
    backboard()
    poll()


def rim():
    glPushMatrix()
    glRotatef(90, 200, 2, 2)
    glColor3f(1.0, .64, 0)
    glTranslatef(0, 0, 1)
    numc = 100
    numt = 100
    TWOPI = 2 * math.pi

    for i in range(numc):
        glBegin(GL_QUAD_STRIP)
        for j in range(numt):
            for k in range(1, 0, -1):
                s = (i + k) % numc + 0.5
                t = j % numt
                xs = (1 + 0.1 * math.cos(s * TWOPI / numc)) * math.cos(t * TWOPI / numt)
                y = (1 + 0.1 * math.cos(s * TWOPI / numc)) * math.sin(t * TWOPI / numt)
                z = 0.1 * math.sin(s * TWOPI / numc)

                glVertex3d(xs, y, 2 * z)
        glEnd()
    glPopMatrix()


def backboard():
    glPushMatrix()
    glRotate(90, 1, 0, 0)
    glScalef(1 / 2, 3, 2.5)
    glTranslatef(3, 0, 0)
    glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()
    glScalef(1 / 2.5, 2, 1)
    glPopMatrix()


def poll():
    glPushMatrix()
    glRotate(90, 1, 0, 0)
    glTranslatef(1.5, 0, 1)
    glColor3f(1, 1, 1)
    quadratic = gluNewQuadric()
    gluCylinder(quadratic, .5, .5, 8, 100, 10)
    glPopMatrix()


def basketball():
    glPushMatrix()
    quad = gluNewQuadric()
    glColor3f(1.0, .64, 0)
    gluSphere(quad, .4, 100, 10)
    glPopMatrix()
