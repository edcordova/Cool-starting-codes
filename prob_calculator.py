#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator
#Instructions to this code

import copy
import random
from random import randint
# Consider using the modules imported above.

class Hat:
  
  def __init__(self,**kwargs):
    
    self.aux_list=[]
    form=''
    for keys,values in kwargs.items():
      form+=(keys+' ')*values
      self.contents=form.split()
           
    
    
  def draw(self,balls_draw):
      i=0
      while i<balls_draw:
        if len(self.contents)>=balls_draw:
          index=randint(0,len(self.contents))
          ball_drawn=self.contents.pop(index)
          self.aux_list.append(ball_drawn)
          i+=1
        else: 
          return self.aux_list #en caso de no ser asi devolver las bolas al sombrero y continuar con el draw
        

h=Hat(blue=1,red=2,black=4)
h.draw(3)


#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
