from pygame import *
'''variables'''
background_color = (200,255,255)
width = 700
height = 500
window = display.set_mode((width,height))
window.fill(background_color)
clock = time.Clock()

game = True 
while game:
 for e in event.get():
  if e.type == QUIT:
   game = False
 display.update()
 clock.tick(60)
