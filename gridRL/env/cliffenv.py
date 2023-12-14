import numpy as np
''' 
description

MIT Press, Cambridge, MA, 2018에 기술된 CLiff environment입니다. 

- Environment : 5 x 9 grid
    * Initial State : [0,4] 
    * Terminal State: [8,4] ; R +100
    * Penalty State : [1,4] ~ [7,4] ; R-100
    * 그 외 state : [n,n] ; R-1

    |     |      |      |      |      |      |      |      |    |
    |     |      |      |      |      |      |      |      |    |
    |     |      |      |      |      |      |      |      |    |
    |     |      |      |      |      |      |      |      |    |
    |start| -100 | -100 | -100 | -100 | -100 | -100 | -100 |Goal|
    
- Action Space : left/ right/ up/ down

- Observation Space : [x,y]

    | Num | Observation                          | Min  |     Max      | 
    |-----|--------------------------------------|------|--------------|
    | x   | X position                           | 0    | len(width)   |
    | y   | Y position                           | 0    | len(heights) | 

'''


class Cliffenv():
    def __init__(self):
        self.action_grid = ([0, -1], [0, 1], [1, 0], [-1, 0])  # up, down, right, left
        self.width = 9
        self.height = 5
        self.goal_state = [8, 4]
        self.penalty_state = [[x, 4] for x in range(1, 8)]
        self.initial_state = [0, 4]

    def step(self, state, action):
        x, y = state

        x += action[0]
        y += action[1]

        if x < 0:
            x = 0
        elif x > self.width - 1:
            x = self.width - 1

        if y < 0:
            y = 0
        elif y > self.height - 1:
            y = self.height - 1

        state_ = [x, y]

        if state_ == self.goal_state:
            reward = 100
            done = True
        elif state_ in self.penalty_state:
            reward = -100
            done = True
        else:
            reward = -1
            done = False

        return state_, reward, done

    def reset(self):
        return self.initial_state

