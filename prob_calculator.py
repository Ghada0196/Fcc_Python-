import copy
import random
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **kwargs):
    self.contents = list()
    for (color, num) in kwargs.items():
      for i in range(num):
        self.contents.append(color)

  def draw(self, number):
    self.balls = list()
    if len(self.contents) > number:
      for i in range(number):
        ball = random.choice(self.contents)
        self.contents.remove(ball)
        self.balls.append(ball)
      return self.balls
    else:
      return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for i in range(num_experiments):
    copy_hat = []
    copy_hat = copy.deepcopy(hat)
    balls_drawn = copy_hat.draw(num_balls_drawn)
   
    presence = True
    for (color, n) in expected_balls.items():
      for k in range(n):
        if color in balls_drawn:
          balls_drawn.remove(color)
        else:
          presence = False
    if presence:
      m += 1
  return m/num_experiments
    
