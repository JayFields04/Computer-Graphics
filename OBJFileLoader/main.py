# Pygame and OpenGL
import sys
import pygame
from pygame.constants import *
from OpenGL.GLU import *
# IMPORT OBJECT LOADER
from OBJFileLoader.objloader import *
# Stars
from OBJFileLoader.stars import *
# Fence
from OBJFileLoader.Fence import *
# Basketball Hoop
from OBJFileLoader.hoop import *
# Message Box
from OBJFileLoader.controls import *
import time
# Garage Door
from OBJFileLoader.garage_door import *
# Wii Character
from OBJFileLoader.person import *


def obj_lighting():
    glLightfv(GL_LIGHT0, GL_POSITION, (-40, 200, 100, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)


def main():
    pygame.init()
    viewport = (800, 600)
    pygame.display.set_caption("Floating Island")
    screen = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
    obj_lighting()
    # LOAD OBJECT AFTER PYGAME INIT
    obj = OBJ('FloatingIsland.obj')
    obj.generate()
    house = OBJ('house.obj')
    house.generate()
    garage = OBJ('garage_n_driveway.obj')

    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    wid, hei = viewport
    gluPerspective(90.0, wid / float(hei), 1, 300)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    # Movement and Cam rotation/zoom
    rx, ry = (0, 0)
    tx, ty = (0, 0)
    hoopX, hoopZ = (0, 0)
    zpos = 5
    rotate = move = move_hoop =False
    # Original Cam View
    count = 1
    eyeX, eyeY, eyeZ = (0, 5, 30)
    centerX, centerY, centerZ = (0, 0, 0,)
    upX, upY, upZ = (0, 1, 0)
    # Open Garage Door Parameters
    r_angle, rotateX, rotateY, rotateZ = (0, 0, 0, 0)
    trX, trY, trZ = (0, 0, 0)
    # Shooting Basketball
    ballx, bally, ballz = (-7, -4, 0)
    # Character Position
    wiiX, wiiY, wiiZ = (-2, 0, -1)
    while 1:
        clock.tick(30)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4:
                    zpos = max(1, zpos - 1)
                elif e.button == 5:
                    zpos += 1
                elif e.button == 1:
                    rotate = True
                elif e.button == 3:
                    move = True
                elif e.button ==2:
                    move_hoop = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1:
                    rotate = False
                elif e.button == 3:
                    move = False
                elif e.button == 2:
                    move_hoop = False
            elif e.type == MOUSEMOTION:
                i, j = e.rel
                if rotate:
                    rx += i
                    ry += j
                if move:
                    tx += i
                    ty -= j
                if move_hoop:
                    hoopX += j/30
                    hoopZ += i/30
            elif e.type == KEYDOWN and e.key == K_SPACE and (count % 2) == 1:
                eyeX, eyeY, eyeZ = (0, 25, -35)
                centerX, centerY, centerZ = (0, 0, 0,)
                upX, upY, upZ = (0, 1, 0)
                count += 1
            elif e.type == KEYDOWN and e.key == K_SPACE and (count % 2) == 0:
                eyeX, eyeY, eyeZ = (0, 5, 30)
                centerX, centerY, centerZ = (0, 0, 0,)
                upX, upY, upZ = (0, 1, 0)
                count += 1
            elif e.type == KEYDOWN and e.key == K_UP:
                r_angle, rotateX, rotateY, rotateZ = (90, 1, 0, 0)
                trX, trY, trZ = (0, 2.5, 0)
            elif e.type == KEYDOWN and e.key == K_DOWN:
                r_angle, rotateX, rotateY, rotateZ = (0, 0, 0, 0)
                trX, trY, trZ = (0, 0, 0)
            elif e.type == KEYDOWN and e.key == K_w:
                for i in range(-7, -3, 1):
                    for j in range(-4, -2, 1):
                        for k in range(-2, -1, 1):
                            ballx += .1
                            bally += 1
            elif e.type == KEYDOWN and e.key == K_s:
                for i in range(-7, -3, 1):
                    for j in range(-4, -2, 1):
                        for k in range(-2, -1, 1):
                            ballx += .1
                            bally -= 1
            elif e.type == KEYDOWN and e.key == K_LEFT:
                wiiX -= 1
            elif e.type == KEYDOWN and e.key == K_RIGHT:
                wiiX += 1
            elif e.type == KEYDOWN and e.key == K_r:
                # Shooting Basketball
                ballx, bally, ballz = (-7, -4, 0)
                # Character Position
                wiiX, wiiY, wiiZ = (-2, 0, -1)
            elif e.type == KEYDOWN and e.key == K_h:
                message()
            elif e.type == KEYDOWN and e.key == K_1:
                eyeX, eyeY, eyeZ = (-30, 15, -10)
                centerX, centerY, centerZ = (0, 0, 0,)
                upX, upY, upZ = (0, 1, 0)
            elif e.type == KEYDOWN and e.key == K_2:
                eyeX, eyeY, eyeZ = (30, 15, -10)
                centerX, centerY, centerZ = (0, 0, 0,)
                upX, upY, upZ = (0, 1, 0)
            elif e.type == KEYDOWN and e.key == K_3:
                eyeX, eyeY, eyeZ = (0, 30, -10)
                centerX, centerY, centerZ = (0, 0, 0,)
                upX, upY, upZ = (0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ)
        # RENDER OBJECT
        glTranslate(tx / 20., ty / 20., - zpos)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)

        # Floating Island
        glTranslate(1, 1, -10)
        obj.render()
        # House
        glTranslate(1, -1, 1)
        glScalef(2, 2, 2)
        house.render()
        glScalef(1 / 2, 1 / 2, 1 / 2)
        # Garage and Driveway
        glTranslate(3 * 1.5, 1, 1)
        glScalef(1.5 * 2, 1 * 2, 1 * 2)
        garage.render()
        glScalef(1 / (1.5 * 2), 1 / (1 * 2), 1 / (1 * 2))
        # Fence
        glTranslate(-7, 0, 30)
        glScalef(25, 1, 50)
        draw_fence()
        glScalef(1 / 25, 1, 1 / 50)
        # Garage Door Open
        door(r_angle, rotateX, rotateY, rotateZ, trX, trY, trZ)
        # Hoop
        glPushMatrix()
        glTranslatef(20, 8, -8)
        glTranslate(hoopX, 0, hoopZ)
        # glRotate(-90, 0, 1, 0)
        basketball_hoop()
        glPopMatrix()
        # Basketball
        glTranslatef(20, 8, -8)
        glTranslatef(ballx, bally, ballz)
        basketball()

        # Wii Character
        # glTranslatef(20, 8, -8)
        wii_character(wiiX, wiiY, wiiZ)
        # Moving Stars
        num1, num2 = rand_coord()
        for i in num1:
            for j in num2:
                stars(i, j)

        pygame.display.flip()


if __name__ == "__main__":
    message()
    time.sleep(1)
    main()
