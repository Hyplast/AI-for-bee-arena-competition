import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np

class BeeArena(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.MultiDiscrete(8,4)
        self.observation_space = spaces.Discrete(49)

#       self.name = 'beearena'
#       self.n_players = 2
#       self.grid_length = 30
#       self.grid_height = 25
#       self.num_squares = self.grid_lenght * self.grid_height
#       self.grid_shape = (self.grid_length, self.grid_height)

# 5 bees, 2 hives, 30-40 flowers
# Arena is 25 rows * 30 columns
# Vision of a bee is 3 r = 49 tiles
#
# MOVE = 0
# FORAGE = 1
# BUILD = 2
# GUARD = 3
#
# N = 0
# NE = 1
# E = 2
# SE = 3
# S = 4
# SW = 5
# W = 6
# NW = 7
#
# EMPTY = 0
# BEE_0 = 1
# BEE_1 = 2
# BEE_0_WITH_FLOWER = 3
# BEE_1_WITH_FLOWER = 4
# FLOWER = 5
# WALL = 6
# HIVE_0 = 7
# HIVE_1 = 8
# OUTSIDE = 9
#

    def step(self, action):
        state = 1

        reward = np.random.normal(loc = action, scale = action)

        done = True

        info = {}

        return state, reward, done, info

    def reset(self):
        state = 0
        return state

    def render(self, mode='human'):
        pass

    def close(self):
        pass
