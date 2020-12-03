from OpenGL.GL import *


def draw_fence():
    glLineWidth(7)
    glColor3f(1, 1, 1)
    draw_frontwall()
    draw_backwall2()
    draw_sidewall1()
    draw_sidewall2()


def draw_backwall():
    glPushMatrix()
    glColor3f(1, 1, 1)
    glRotatef(180, 0.0, 1.0, 0.0)
    glTranslatef(0.0, 0.0, -0.1)
    draw_frontwall()
    glPopMatrix()


def draw_frontwall():
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glEnd()
    glPopMatrix()


def draw_backwall2():
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()


def draw_sidewall1():
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    glVertex3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 0.0)
    glEnd()
    glPopMatrix()


def draw_sidewall2():
    glPushMatrix()
    glBegin(GL_LINE_LOOP)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, 0.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()
    glPopMatrix()


def fence():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glLoadIdentity()
    glTranslatef(1.0, -2.0, -10.0)

    verticies = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
