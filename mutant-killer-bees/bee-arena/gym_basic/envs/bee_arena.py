import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

MOVE = 0
FORAGE = 1
BUILD = 2
GUARD = 3

EMPTY = 0
BEE_0 = 1
BEE_1 = 2
BEE_0_WITH_FLOWER = 3
BEE_1_WITH_FLOWER = 4
FLOWER = 5
WALL = 6
HIVE_0 = 7
HIVE_1 = 8
OUTSIDE = 9

N = 0
NE = 1
E = 2
SE = 3
S = 4
SW = 5
W = 6
NW = 7

class BeeArena(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.MultiDiscrete([8,4])
        self.observation_space = spaces.Box(
            low=EMPTY,
            high=OUTSIDE,
            shape=(49,),
            dtype=np.float32
        )
# [0,9,49,56435]
        self.name = 'beearena'
        self.state = 0
        self.action2str = [N,NE,E,SE,S,SW,W,NW]
        self.n_players = 2
        self.grid_length = 30
        self.grid_height = 25
        self.ep_length = 1000
        self.current_step = 0
        self.num_squares = self.grid_length * self.grid_height
        self.grid_shape = (self.grid_length, self.grid_height)

# 5 bees, 2 hives, 30-40 flowers
# Arena is 25 rows * 30 columns
# Vision of a bee is 3 r = 49 tiles

    def step(self, action):

        #print(self)

        #state = 1
        self.current_step += 1
        done = self.current_step >= self.ep_length
        #print(state)
        #print(action)
        # print(action[1])
        # print("equals")
        # print(action)
        if action[0] == NE and action[1] == MOVE:
            reward = 1
        else:
            reward = -1

        info = {}
        #state = self.observation_space.sample()
        ret = np.array(
                [9,9,9,9,9,9,9,
                9,5,0,0,0,0,9,
                9,0,0,0,0,0,9,
                9,0,0,1,0,0,9,
                9,0,0,0,0,0,9,
                9,0,0,0,0,0,9,
                9,9,9,9,9,9,9] ) 
        #print(state)
        #print(ret)
        state = ret
        return state, reward, done, info
        # return 1, 1, True, {}

    def reset(self) -> np.array:
        #state = np.array[self.observation_space]
        #state = np.array(0,9999999888888877777776666666555555544444443333333)
        #self.state = 0
        self.current_step = 0
        ret = np.array( [9,9,9,9,9,9,9,
                        9,5,0,0,0,0,9,
                        9,0,0,0,0,0,9,
                        9,0,0,1,0,0,9,
                        9,0,0,0,0,0,9,
                        9,0,0,0,0,0,9,
                        9,9,9,9,9,9,9] ) 
        #self.observation_space = ret
        #print("dim:", ret.size)
        return ret
        #return self.observation_space.sample()
        #return self.observation_space.sample()
        #return self.step(np.ndarray([0, 0, 0, 0]))[0]
        # state
        # if not return_info:
        #             return self.step(np.array([0, 0, 0, 0]))[0]
        #         else:
        #             return self.step(np.array([0, 0, 0, 0]))[0], {}
    def render(self, mode='human'):
        pass

    def close(self):
        pass
