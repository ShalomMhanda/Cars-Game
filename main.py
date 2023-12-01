from graphics import *
from cars import *
import random
import time

def level1(win):
  score_count = 0
  ## TEXT ##
  text_colors = ["red" , "green" , "blue"]
  number = random.randint(0, 2)
  text_color = text_colors[number]
  word_color = text_color

  newtext = TextPrompt(Point(300, 50), win, text_color, word_color)
  newtext.draw(win)

  ## TEXT ^ ##

  ## CAR ##
  count = 0
  while count <= 20:
    colors = ["red" , "green" , "blue"]
    num = random.randint(0, 2)
    car_color = colors[num]

    newcar = Car(Point(0, 300), win, car_color)
    newcar.draw(win)

    dx = 1
    dy = 0

    while newcar.body.getCenter().getX() <= 640:
      newcar.move(dx, dy)

      update(200)

    user_click = win.checkMouse()
    if user_click:
      if number == num:
        score_count += 1
        print("Good Choice!", score_count)
        newtext.undraw()
        text_colors = ["red" , "green" , "blue"]
        number = random.randint(0, 2)
        text_color = text_colors[number]
        word_color = text_color

        newtext = TextPrompt(Point(300, 50), win, text_color, word_color)
        newtext.draw(win)
      
      else:
        print("Try again :(")

    
    count += 1
    time.sleep(1.0)
  

  ## CAR ^ ##

  newtext.undraw()

  return score_count
  

def level2(win):
  score_count = 0
  ## TEXT ##
  text_colors = ["red" , "green" , "blue", "yellow", "orange", "purple"]
  number = random.randint(0, 5)
  text_color = text_colors[number]
  word_color = text_color

  newtext = TextPrompt(Point(300, 50), win, text_color, word_color)
  newtext.draw(win)

## TEXT ^ ##

## CAR ##
  count = 0
  while count <= 40:
    colors = ["red" , "green" , "blue", "yellow", "orange", "purple"]
    num = random.randint(0, 5)
    car_color = colors[num]

    newcar = Car(Point(0, 300), win, car_color)
    newcar.draw(win)

    dx = 1
    dy = 0

    while newcar.body.getCenter().getX() <= 640:
      newcar.move(dx, dy)

      update(600)

    user_click = win.checkMouse()
    if user_click:
      if number == num:
        score_count += 1
        print("Nice Job!", score_count)
        newtext.undraw()
        text_colors = ["red" , "green" , "blue", "yellow", "orange", "purple"]
        number = random.randint(0, 5)
        text_color = text_colors[number]
        word_color = text_color

        newtext = TextPrompt(Point(300, 50), win, text_color, word_color)
        newtext.draw(win)
      else:
        print("Wrong :(")

    
    count += 1
    time.sleep(1.0)

  ## CAR ^ ##
  newtext.undraw()
  return score_count

def level3(win):
  score_count = 0
  ## TEXT ##
  text_colors = ["red" , "green" , "blue", "yellow", "orange", "purple", "white", "black", "brown"]
  number = random.randint(0, 8)
  text_color = text_colors[number]

  number2 = random.randint(0,8)
  word_color = text_colors[number2]

  newtext = TextPrompt(Point(300, 50), win, text_color, word_color)
  newtext.draw(win)

## TEXT ^ ##

## CAR ##
  count = 0
  while count <= 40:
    colors = ["red" , "green" , "blue", "yellow", "orange", "purple", "white", "black", "brown"]
    num = random.randint(0, 8)
    car_color = colors[num]

    newcar = Car(Point(0, 300), win, car_color)
    newcar.draw(win)

    dx = 1
    dy = 0

    while newcar.body.getCenter().getX() <= 640:
      newcar.move(dx, dy)

      update(1000)

    user_click = win.checkMouse()
    if user_click:
      if number == num:
        score_count += 1
        print("Great!", score_count)
        newtext.undraw()
        text_colors = ["red" , "green" , "blue", "yellow", "orange", "purple", "white", "black", "brown"]
        number = random.randint(0, 8)
        text_color = text_colors[number]

        number2 = random.randint(0,8)
        word_color = text_colors[number2]

        newtext = TextPrompt(Point(300, 50), win, text_color, word_color)
        newtext.draw(win)
      else:
        score_count -= 1
        print("Seriously? No. >:(", score_count)

    
    count += 1


  ## CAR ^ ##
  newtext.undraw()
  return score_count

def main():

  width = 600
  height = 400
  win = GraphWin("Car Game", width, height)

  bg = Image(Point(300,200), "img/bgroad1.png")
  Image.draw(bg, win)

  
  again = 'yes'

  lvl = int(input("Which level would you like to play? (1, 2, or 3) "))

  while again != "no":

    if lvl == 1:
      print("Click the car that corresponds to the color prompt!")
      score_count = level1(win)

      score_text = ScoreText(Point(300, 150), win, score_count)
      score_text.draw(win)
      time.sleep(5)
      score_text.undraw()

    elif lvl == 2:
      print("Click the car that corresponds to the color prompt!")
      score_count = level2(win)

      score_text = ScoreText(Point(300, 150), win, score_count)
      score_text.draw(win)
      time.sleep(5)
      score_text.undraw()

    elif lvl == 3:
      print("Click the car that corresponds to the color written (not the color of the word)!")
      score_count = level3(win)

      score_text = ScoreText(Point(300, 150), win, score_count)
      score_text.draw(win)
      time.sleep(5)
      score_text.undraw()

    else:
      print("You entered an invalid level. ")
      lvl = int(input("Which level would you like to play? (1, 2, or 3) "))
      
    again = input("Would you like to play again? (yes/no) ")
    lvl = int(input("Which level would you like to play? (1, 2, or 3) "))
  

  win.close()
  exit()


if __name__ == '__main__':
  main()