import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys

class Base(object):
   def __init__(self, tamanhoTela=[320, 320]):
      pygame.init()
      self.tela = pygame.display.set_mode(tamanhoTela, pygame.DOUBLEBUF | pygame.OPENGL )
      gluOrtho2D( 0, 320, 0, 320)
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
   
   def linhas(self):
      glBegin(GL_LINES)
      glColor3f(1,0,0)
      #linha L -> R
      glVertex2i(0, 160)
      glVertex2i(150, 160)
      #linha R -> L
      glVertex2i(170, 160)
      glVertex2i(320, 160)
      #linha T -> D
      glVertex2i(160, 0)
      glVertex2i(160, 150)
      #linha D -> T
      glVertex2i(160, 320)
      glVertex2i(160, 170)
      
      #lado L
      glVertex2i(60, 70)
      glVertex2i(60, 250)

      #lado R
      glVertex2i(260, 70)
      glVertex2i(260, 250)

      #lado T
      glVertex2i(54, 255)
      glVertex2i(265, 255)  

      #lado D
      glVertex2i(54, 65)
      glVertex2i(265, 65)      

      glEnd()      
      
   def desenho2(self):
      glClearColor(1.0, 1.0, 0, 0)
      glClear(GL_COLOR_BUFFER_BIT)
      self.linhas()
      glLineWidth(11)

d = Desenho()
d.run()
