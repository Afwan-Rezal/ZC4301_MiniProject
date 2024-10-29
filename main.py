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

cubeMesh = LoadMesh("Objects/cube.obj", GL_TRIANGLES)
domeMesh = LoadMesh("Objects/dome.obj", GL_TRIANGLES)

vertical = cubeMesh
horizontal = cubeMesh
block = cubeMesh
dome = domeMesh


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

def draw_innerFrames():
    # Right Frame
    glPushMatrix()
    glColor3f(1.0, 0.84, 0.0)
    glTranslatef(-7.5, 6.0, 0)
    glScalef(1, 11.0, 0.65)
    vertical.draw()
    glPopMatrix()

    # Left Frame
    glPushMatrix()
    glColor3f(1.0, 0.84, 0.0)
    glTranslatef(7.5, 6.0, 0)
    glScalef(1, 11.0, 0.65)
    vertical.draw()
    glPopMatrix()

    # Top Frame
    glPushMatrix()
    glColor3f(1.0, 0.84, 0.0)
    glTranslatef(0, 10.5, 0)
    glScalef(15.0, 1.0, 0.65)
    horizontal.draw()
    glPopMatrix()

    # Bottom Frame
    glPushMatrix()
    glColor3f(1.0, 0.84, 0.0)
    glTranslatef(0, 1.5, 0)
    glScalef(15.0, 1.0, 0.65)
    horizontal.draw()
    glPopMatrix()


def draw_outerFrames():
    # Right Frame
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(-8.0, 6.0, 0)
    glScalef(1, 12.2, 1.0)
    vertical.draw()
    glPopMatrix()

    # Left Frame
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(8.0, 6.0, 0)
    glScalef(1, 12.2, 1.0)
    vertical.draw()
    glPopMatrix()

    # Top Frame
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(0, 11.5, 0)
    glScalef(15.0, 1.2, 1.0)
    horizontal.draw()
    glPopMatrix()

    # Bottom Frame
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(0, 0.5, 0)
    glScalef(15.0, 1.2, 1.0)
    horizontal.draw()
    glPopMatrix()


def draw_mosque():

    # Layer 1: Block and pillars

    # Right-Front Pillar
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(-8.0, 5.5, 100)
    glScalef(1.0, 11.0, 1.0)
    vertical.draw()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.84, 0.0)
    glTranslatef(-8.0, 11.0, 100)
    glRotate(270, 1, 0, 0)
    dome.draw()
    glPopMatrix()

    # Left-Front Pillar
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(8.0, 5.5, 100)
    glScalef(1.0, 11.0, 1.0)
    vertical.draw()
    glPopMatrix()

    glPushMatrix()
    glColor3f(1.0, 0.84, 0.0)
    glTranslatef(8.0, 11.0, 100)
    glRotate(270, 1, 0, 0)
    dome.draw()
    glPopMatrix()

    # Block
    glPushMatrix()
    glColor3f(1.0, 1.0, 1.0)
    glTranslatef(0, 5, 105)
    glScalef(15, 9.5, 10.5)
    vertical.draw()
    glPopMatrix()




def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera_init()
    draw_world_axes()

    # Drawing the Frames
    draw_innerFrames()
    draw_outerFrames()

    draw_mosque()


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
