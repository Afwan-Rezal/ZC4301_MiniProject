from pygame.locals import *
from Utilities.LoadMesh import *
from Utilities.Camera import *

import os

x = 850
y = 200
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

camera = Camera()

cubeMesh = LoadMesh("Objects/cube.obj", GL_LINE_LOOP)
domeMesh = LoadMesh("Objects/dome.obj", GL_LINE_LOOP)

# BIBD Frames Objects
leftFrame = cubeMesh
rightFrame = cubeMesh
topFrame = cubeMesh
botFrame = cubeMesh

# Mosque Objects
pillar1 = cubeMesh
pillar2 = cubeMesh
pillar3 = cubeMesh
pillar4 = cubeMesh
longPillar = cubeMesh
smallBlock = cubeMesh
bigBlock = cubeMesh
mainBlock = cubeMesh

pilDom1 = domeMesh
pilDom2 = domeMesh
pilDom3 = domeMesh
pilDom4 = domeMesh
longPilDom = domeMesh
mainDom = domeMesh


def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 1000.0)


def camera_init():
    # modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    camera.update()


def draw_world_axes():
    glLineWidth(4)
    glBegin(GL_LINES)

    glColor(1, 0, 0)
    glVertex3d(-1000, 0, 0)
    glVertex3d(1000, 0, 0)

    glColor(0, 1, 0)
    glVertex3d(0, -1000, 0)
    glVertex3d(0, 1000, 0)

    glColor(0, 0, 1)
    glVertex3d(0, 0, -1000)
    glVertex3d(0, 0, 1000)

    glEnd()

    sphere = gluNewQuadric()

    # x pos sphere
    glColor(1, 0, 0)
    glPushMatrix()
    glTranslated(1, 0, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # y pos sphere
    glColor(0, 1, 0)
    glPushMatrix()
    glTranslated(0, 1, 0)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    # z pos sphere
    glColor(0, 0, 1)
    glPushMatrix()
    glTranslated(0, 0, 1)
    gluSphere(sphere, 0.05, 10, 10)
    glPopMatrix()

    glLineWidth(1)
    glColor(1, 1, 1)


# Building Blocks

def draw_frames():
    # Left Frame
    glPushMatrix()
    glTranslatef(-8.0, 5.5, 0)  # Corrected position for the left frame (negative X)
    glScalef(1.0, 11.0, 1.0)
    leftFrame.draw()
    glPopMatrix()

    # Right Frame
    glPushMatrix()
    glTranslatef(8.0, 5.5, 0)  # Corrected position for the right frame (positive X)
    glScalef(1.0, 11.0, 1.0)
    rightFrame.draw()
    glPopMatrix()

    # Top Frame
    glPushMatrix()
    glTranslatef(0, 10.5, 0)  # Position for the top frame (positive Y)
    glScalef(15.0, 1.0, 1.0)
    topFrame.draw()
    glPopMatrix()

    # Bottom Frame
    glPushMatrix()
    glTranslatef(0, 0.5, 0)  # Position for the bottom frame
    glScalef(15.0, 1.0, 1.0)
    botFrame.draw()
    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera_init()
    draw_world_axes()

    # Drawing the Frames
    draw_frames()

    # Draw mesh2 without scaling
    glPushMatrix()
    glTranslatef(0, 4.0, 0)  # Adjust '2.0' as needed to control the stacking height
    # mesh2.draw()
    glPopMatrix()


done = False
initialise()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)
            if event.key == K_SPACE:
                pygame.mouse.set_visible(False)
                pygame.event.set_grab(True)
    display()
    pygame.display.flip()
    pygame.time.wait(60);
pygame.quit()
