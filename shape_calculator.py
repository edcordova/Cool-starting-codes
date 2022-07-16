#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator
#instructions to this code

class Rectangle:

  def __init__ (self, width,height):
    self.width=width
    self.height=height
  def set_width(self,width):
    self.width=width
  def set_height(self, height):
    self.height=height
  def get_area(self):
    self.area=self.width*self.height
    return self.area
  def get_perimeter(self):
    self.perimeter=(2 * self.width) + (2 * self.height)
    return self.perimeter
  def get_diagonal(self):
    self.diagonal=((self.width ** 2 + self.height ** 2) ** 0.5)
    return self.diagonal
  def get_picture(self):
    if self.height<=50 and self.width<=50:
      j=0
      self.picture=''
      while j<self.height:
        self.picture+='*'*self.width+'\n'
        j+=1
      return self.picture
    else: return 'Too big for picture.'
  #Returns the number of times the passed in shape could fit inside the shape (with no rotations).
  def get_amount_inside(self,figure):
    
    hornumber=(self.width) /figure.width
    print(hornumber)
    vernumber=(self.height)/figure.height
    print(vernumber)
    if vernumber<1 or hornumber<1:
      numberoftimes=0
    else:
      numberoftimes=int(hornumber*vernumber)
    return numberoftimes
  def __str__(self):
    representacion=f'Rectangle(width={self.width}, height={self.height})'
    return representacion
#################################################
    
class Square(Rectangle):
  def __init__ (self,side):
    self.side=side
    self.width=side
    self.height=side
  def set_side(self,side):
    super().set_height(side)
    super().set_width(side)
    self.side=side
    
  def set_width(self, width):
    self.set_side(width)
  def set_height(self,height):
    self.set_side(height)
  def __str__(self):
    representacion=f'Square(side={self.side})'
    return representacion