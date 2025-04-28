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
        glBegin(GL_LINE_STRIP)
        
        #linha Verde
        glColor3f(0, 1, 0)
        glVertex2f(160, 260)
        glVertex2f(190, 170)
        
        #linha Azul
        glColor3f(0, 0, 1)
        glVertex2f(245, 95)
        glVertex2f(160, 125)
        
        #linha Vermelha
        glColor3f(1, 0, 0)
        glVertex2f(75, 95)
        glVertex2f(130, 170)
        
        #Ponto inicial
        glColor3f(0, 1, 0)
        glVertex2f(160, 260)


        glEnd()
      
   def desenho2(self):
      glClearColor(0, 0, 0, 0)
      glClear(GL_COLOR_BUFFER_BIT)
      self.linhas()
      glLineWidth(4)

d = Desenho()
d.run()
