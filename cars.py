import random
from graphics import *

class Car:
  def __init__(self, position, win, color):
    self.construct(position, win, color)
  
  def construct(self, position, win, color):
    # car body
    p1 = Point(position.getX()-40, position.getY()-20)
    p2 = Point(position.getX()+40, position.getY()+20)
    self.body = Rectangle(p1, p2)
    self.body.setFill(color)
    
    #front tire
    p1 = Point(position.getX()+30, position.getY()+20)
    self.ftire = Circle(p1, 10)
    self.ftire.setFill("black")

    #back tire 
    p1 = Point(position.getX()-30, position.getY()+20)
    self.btire = Circle(p1, 10)
    self.btire.setFill("black")
  
  def draw(self, win):
    self.body.draw(win)
    self.ftire.draw(win)
    self.btire.draw(win)

  def undraw(self):
    self.body.undraw()
    self.ftire.undraw()
    self.btire.undraw()

  def move(self, dx, dy):
    self.body.move(dx, dy)
    self.ftire.move(dx, dy)
    self.btire.move(dx, dy)

class TextPrompt:
  def __init__(self, position, win, color, word_color):
    self.construct(position, win, color, word_color)
  

  def construct(self, position, win, color, word_color):
    
    p1 = Point(position.getX(), position.getY())
    self.text_body = Text(p1, color)
    self.text_body.setFill(word_color)

  
  def draw(self, win):
    self.text_body.draw(win)

  def undraw(self):
    self.text_body.undraw()


class ScoreText:
  def __init__(self, position, win, score):
    self.construct(position, win, score)
  
  def construct(self, position, win, score):
    
    p1 = Point(position.getX(), position.getY())
    self.tbody = Text(p1, score)
    self.tbody.setSize(36)
    self.tbody.setStyle("bold")
    self.tbody.setFill("black")

  def draw(self, win):
    self.tbody.draw(win)

  def undraw(self):
    self.tbody.undraw()
