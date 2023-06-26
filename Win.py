import turtle
from random import random
import time

def winner():
  # Create a turtle object: pen
  pen = turtle.Turtle()
  pen.shape("turtle")
  pen.speed(8)
  # Define method to draw circle 
  def ring(col, rad):
      # Set fill
      pen.fillcolor(col)
      # Start filling the color
      pen.begin_fill()
      # Draw circle
      pen.circle(rad)
      # End the filling of the color
      pen.end_fill()

  # Draw first ear
  pen.up()
  pen.setpos(-65, 185)
  pen.down
  ring('black', 30)
    
  # Draw second ear
  pen.up()
  pen.setpos(65, 185)
  pen.down()
  ring('black', 30)
    
  pen.up()
  pen.setpos(0, 76)
  pen.down()
  ring('white', 70)
    
  # Draw first eye (black)
  pen.up()
  pen.setpos(-36, 150)
  pen.down
  ring('black', 12)
    
  # Draw second eye (black)
  pen.up()
  pen.setpos(36, 150)
  pen.down()
  ring('black', 12)
    
  # Draw first eye (white)
  pen.up()
  pen.setpos(-36, 151)
  pen.down()
  ring('white', 6)
    
  # Draw second eye (white)
  pen.up()
  pen.setpos(36, 151)
  pen.down()
  ring('white', 6)
    
  # Draw nose 
  pen.up()
  pen.setpos(0, 110)
  pen.down
  ring('black', 10)

  # Draw mouth
  pen.up()
  pen.setpos(0, 110)
  pen.down()
  pen.right(90)
  pen.circle(10, 180)
  pen.up()
  pen.setpos(0, 110)
  pen.down()
  pen.left(360)
  pen.circle(10, -180)
  pen.hideturtle()

  turtle.hideturtle()
  turtle.color(random(), random(), random())
  style = ("Courier", 20, 'italic' )
  turtle.write("Congratulations, you are an animal genius :)", font = (style), align = "center")
  time.sleep(2)
  turtle.clear()

  turtle.color('black')
  style = ("Courier", 16)
  turtle.write("This is your reward: A surprise animal!", font = style, align = 'center')
  time.sleep(2)
  turtle.clear()

  style = ("Courier", 15)
  turtle.write("Hi, I am a panda", font = style, align = "center")
  time.sleep(2)
  turtle.clear()

  style = ("Courier", 14)
  turtle.write ("I am the main character in Kung Fu Panda", font = style, align = "center")
  time.sleep(2)
  turtle.clear()

  turtle.write("I like eating bamboo and sleeping", font = style, align = "center")
  time.sleep(2)
  turtle.clear()

  turtle.write("I sometimes do handstands when I wee", font = style, align = "center")

  turtle.exitonclick()    