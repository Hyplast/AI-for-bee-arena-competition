import gym
from gym import error, spaces, utils
from gym.utils import seeding

class BasicEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.action_space = spaces.Discrete(5)
        self.observation_space = spaces.Discrete(2)

# 5 bees, 2 hives, 30-40 flowers
# Arena is 25 rows * 30 columns
# Vision of a bee is 3 r = 49 tiles
#
# 0 MOVE
# 1 FORAGE
# 2 BUILD
# 3 GUARD
#
# 0 N
# 1 NE
# 2 E
# 3 SE
# 4 S
# 5 SW
# 6 W
# 7 NW
#
# 0 EMPTY
# 1 BEE_0
# 2 BEE_1
# 3 BEE_0_WITH_FLOWER
# 4 BEE_1_WITH_FLOWER
# 5 FLOWER
# 6 WALL
# 7 HIVE_0
# 8 HIVE_1
# 9 OUTSIDE
#

    def step(self, action):
        state = 1

        if action == 0:
            reward = 1
        else:
            reward = -1

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
