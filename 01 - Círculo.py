import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import gluOrtho2D
import math

def init_display(width=800, height=600):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(0, width, 0, height)
    glPointSize(2)

def draw_point(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()

def polar(center_x, center_y, radius):
    glColor3f(1.0, 1.0, 1.0)
    for angle in range(0, 360):
        theta = math.radians(angle)
        x = center_x + radius * math.cos(theta)
        y = center_y + radius * math.sin(theta)
        draw_point(x, y)

def midpoint(center_x, center_y, radius):
    glColor3f(2.0, 0.5, 1.0)
    x = 0
    y = radius
    param = 1 - radius

    def draw(cx, cy, x, y):
        for dx, dy in [(x, y), (y, x), (-x, y), (-y, x),
                       (-x, -y), (-y, -x), (x, -y), (y, -x)]:
            draw_point(cx + dx, cy + dy)

    draw(center_x, center_y, x, y)
    while x < y:
        x += 1
        if param < 0:
            param += 2 * x + 1
        else:
            y -= 1
            param += 2 * (x - y) + 1
        draw(center_x, center_y, x, y)

def main():
    init_display()
    running = True

    while running:
        glClear(GL_COLOR_BUFFER_BIT)

        polar(250, 300, 100) #círculo branco
        midpoint(550, 300, 100) #círculo rosa

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False

    pygame.quit()

if __name__ == '__main__':
    main()