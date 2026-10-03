import math
class Rectangle:
    def __init__(self,width, height):
        self._width= width
        self._height= height
    def set_width(self,width):
        self._width = width    
    def set_height(self,height):
        self._height = height   
    def get_area(self):
        return self._width * self._height 
    def get_perimeter (self)  :
        return 2* (self._width+ self._height)   
    def get_diagonal(self):
        return math.sqrt(self._width**2+ self._height**2)
    def get_picture(self) :
        if self._width> 50 or self._height> 50:
            return "Too big for picture."
        picture=(("*" * self._width +"\n")* self._height) 
        return picture 
    def get_amount_inside(self,shape):
        return  (self._width // shape._width )*(self._height // shape._height)   
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"
class Square(Rectangle):
    def __init__(self,side):
         super().__init__(side,side)
    def set_side(self,value):
        self._width=value
        self._height=value
    def set_width(self,width):
        self.set_side(width)    
    def set_height(self,height):
        self.set_side(height)     
    def __str__(self):
        return f"Square(side={self._width})"

rect = Rectangle(width=10,height= 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))