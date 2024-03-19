import play #loading the play module library
import pygame #loading the pygame module library
import random #loading the random module library

w = 300 #defining global variable for horizontal size court
h = 400 #defining global variable for vertical size court
hw = w/2 #defining global variable for horizontal size court
hh = h/2 #defining global variable for vertical size court
score = 0 #global variable got points
speed = 3 #global variable for velocity of ball

@play.when_program_starts #this creates a keyframe to start the game function as soon as you press RUN
def do():
  play.set

court = play.new_box(
  color = (255, 242, 252), #set the color a lighter pink
  x = 0, #x coordinate of the court
  y = 0, #y coordinate of the court
  width = w, #use global variable to populate local variable
  height = h, #use global variable to populate local variable
)

ball = play.new_circle(
  color = (255, 105, 180),
  radius = 10,
  x = 0,
  y = hh - 30,
  angle = random.randint(210, 330),
)

paddle = play.new_box(
  color = "black",
  width = 50,
  height = 10,
  x = 0,
  y = -hh +10,
)
#creating a new variable for the text of the score
#and initializing it with a built in function new_text from play module
#creating a variable for the text of the score
#and initializing it with a built in function  new_text from play module
score_test = play.new_text(
  words = "Score: " + str(score),
  x = 0,
  y = hh + 15,
  font = None,
  color = "black",
)

@play.repeat_forever #keyframe to do the following code as long as the game is playing

def do(): #define the function or subroutine
 global score #calling for the global variable score
 paddle.x = play.mouse.x #DOT notation to recall the x parameter of the paddle and reassign value to match mouse X coordinates
  #ensure the paddle is not off the play field
 if(play.mouse.x < -hw + paddle.width/2):
   paddle.x = -hw + paddle.width/2
 if(play.mouse.x > hw - paddle.width/2):
   paddle.x = hw - paddle.width/2
 ball.move(speed)
 #bounce off top/bottom : 360/angle
 #top wall
 if(ball.y + ball.radius > hh):
  ball.angle = 360 - ball.angle
 #bottom wall
 if(ball.y + ball.radius < -hh):
  ball.angle = 360 - ball.angle
  score -= 1
 #bounce off left/right : 180 - angle
 #right wall
 if(ball.x + ball.radius > hw):
  ball.angle = 180 - ball.angle
 #left wall
 if(ball.x - ball.radius < -hw):
  ball.angle = 180 - ball.angle
 # make sure it bounces as if it has hit the bottom, and give it a little change of trajectory
 if(ball.is_touching(paddle)):
  ball.angle = 360 - ball.angle + random.randint(-30,30)
  ball.angle %= 360
  # make sure that the ball goes up after hitting the paddle
  if(ball.angle < 20):
    ball.angle = 20
  elif(ball.angle > 160):
    ball.angle = 160
  score += 1
  if(score == 5):
    paddle.width -= 5

 ball.angle %= 360
 score_test.words = "SCORE: " + str(score)

play.start_program()