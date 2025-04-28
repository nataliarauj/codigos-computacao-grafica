import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

class Base(object):
   def __init__(self, tamanhoTela=[320, 220]):
      pygame.init()
      self.tela = pygame.display.set_mode(tamanhoTela, pygame.DOUBLEBUF | pygame.OPENGL )
      gluOrtho2D( 0, 320, 0, 220)
      self.clock = pygame.time.Clock()

   def initialize(self):
      pass

   def update(self):
      pass
   
   def run(self):
      self.initialize()
      while True:
         self.input()
         self.update()
         pygame.display.flip()
         self.clock.tick(60)

   def input(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Desenho(Base):
   def initialize(self):
      pass
   
   def update(self):
      self.desenho2()  
   
   def quadrados(self):
      glBegin(GL_QUADS)
      glColor3f(0, 0.2, 0.6078)
      
      #Quad T
      glVertex2i(160, 235-45)
      glVertex2i(130, 205-45)
      glVertex2i(160, 175-45)
      glVertex2i(190, 205-45)

      glEnd()

      glBegin(GL_QUADS)
      glColor3f(0, 0, 0)
      
      #Quad D
      glVertex2i(160, 85-45)
      glVertex2i(130, 115-45)
      glVertex2i(160, 145-45)
      glVertex2i(190, 115-45)

      glEnd()

      glBegin(GL_QUADS)
      glColor3f(1,1,0)
      
      #Quad L
      glVertex2i(115, 190-45)
      glVertex2i(85, 160-45)
      glVertex2i(115, 130-45)
      glVertex2i(145, 160-45)

      glEnd()

      glBegin(GL_QUADS)
      glColor3f(1,0,0)
      
      #Quad R
      glVertex2i(205, 190-45)
      glVertex2i(235, 160-45)
      glVertex2i(205, 130-45)
      glVertex2i(175, 160-45)

      glEnd()
     
      
   def desenho2(self):
      glClearColor(0, 1.0, 0, 0)
      glClear(GL_COLOR_BUFFER_BIT)
      self.quadrados()

d = Desenho()
d.run()
