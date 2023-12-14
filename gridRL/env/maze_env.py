import numpy as np
import numpy as np

''' 
description

직접 구현한 환경입니다. 많은 장소에 cliff를 구현하였고, 특정 상태에 도달했을 때 사선으로 미끄러질 수 있는 비탈길을 추가하였습니다. 



- Environment : 5 x 9 grid
    * Initial State : [0,0] 
    * Terminal State: [12,8] ; R +100
    * Penalty State : plot 참조
    * 그 외 state : [n,n] ; R-1


- Action Space : left/ right/ up/ down / 특정상황에서 down&right

- Observation Space : [x,y]

    | Num | Observation                          | Min  |     Max      | 
    |-----|--------------------------------------|------|--------------|
    | x   | X position                           | 0    | len(width)   |
    | y   | Y position                           | 0    | len(heights) | 

'''


class Mazeenv():
    def __init__(self):
        self.height = 9
        self.width = 13
        self.action_grid = [[-1,0],[1,0],[0,-1],[0,1]] # left, right, up, down
        self.initial_state = [0,0]
        self.penalty_state = [
            [1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3],
            [2,6], [2,7], [2,8], [10,5], [11,5], [12,5],
            [4,4], [5,4], [6,4], [5,5], [6,5], [6,6],
            [7,1], [7,2], [8,2], [7,3], [8,3], [9,3]
        ]

        self.shortcut_state = [
            [7,0], [8,1], [9,2], [10,3],
            [3,4], [4,5], [5,6], [6,7]
        ]
        self.reward_state = [
            [12,8]
        ]

    def step(self, state, action, state_memory):
        x,y = state
        x += action[0]
        y += action[1]


        if x < 0:
            x = 0
        elif x > self.width -1:
            x = self.width -1

        if y < 0:
            y = 0
        elif y > self.height -1:
            y = self.height -1


        ### shortcut route ###
        while True:
            if [x,y] in self.shortcut_state:
                print('You are in shortcut state!')
                x+=1; y+=1
            else:
                break

        if [x, y] in self.penalty_state:
            print('You are in penalty states...')
            done = True
            reward = -100
        elif [x,y] in self.reward_state:
            reward = 100
            done = True
        else:
            reward = -1
            done = False

        # state_memorySet = set(map(tuple, state_memory))
        # reward_memory_Set = set(map(tuple, self.reward_state))
        # if len( state_memorySet.intersection(reward_memory_Set)) == len(self.reward_state):
        #     reward = 1000
        #     done = True

        state_ = [x,y]

        return state_, reward, done

    def reset(self):
        return self.initial_state





