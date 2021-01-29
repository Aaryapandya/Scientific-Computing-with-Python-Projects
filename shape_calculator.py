class Rectangle:
  width = 0
  height = 0
  def __init__(self, w, h):
    self.width = w
    self.height = h

  def set_width(self, w):
    self.width = w
  
  def set_height(self, h):
    self.height = h

  def get_area(self):
    return self.width*self.height

  def get_perimeter(self):
    return 2*(self.width+self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if (self.width > 50):
      return "Too big for picture."

    if  (self.height > 50):
      return "Too big for picture."

    i = 0
    res = ""
    while(i<self.height):
      res = res + ('*' * self.width) + '\n'
      i = i + 1 
    
    return res
  

  def __str__(self):
    res = 'Rectangle(width=' + str(self.width) + ', height=' + str(self.height) +')'
    return res
      
  def get_amount_inside(self, shape):
    return int(self.height*self.width/(shape.height*shape.width))


class Square(Rectangle):
  def __init__(self, l):
    Rectangle.__init__(self,l,l)

  def set_side(self, s):
    self.width = s
    self.height = s

  def set_width(self, w):
    self.width = w
    self.height = w
  
  def set_height(self, h):
    self.height = h
    self.width = h

  def __str__(self):
    res = 'Square(side=' + str(self.height) + ')'
    return res

  


