import sys
import libagent
import random
import gym
import time
from stable_baselines3 import DQN
from stable_baselines3.common.env_checker import check_env

def find_neighbour(cells, cell_type):
    for dir in libagent.direction_names:
        (row,col) = libagent.directions_to_offsets[dir]
        if cells[row][col] == cell_type:
            return dir

    return None


def think(info):
    cells = info["cells"]
    bee_cell = cells[0][0]
    has_flower = "WITH_FLOWER" in bee_cell

    if has_flower:
        hive_dir = find_neighbour(cells, "HIVE_%d" % info["player"])
        if hive_dir:
            return {
                'action': "FORAGE",
                'direction': hive_dir
            }

    else:
        flower_dir = find_neighbour(cells, "FLOWER")
        if flower_dir:
            return {
                'action': "FORAGE",
                'direction': flower_dir
            }

#   Load the gym enviroment and AI model and make a prediction
    env = gym.make("gym_basic:basic-v0")
    check_env(env)
    model = DQN.load("MTB")
    obs = env.reset()
    action, _states = model.predict(obs)

    return {
        'action': "MOVE",
        'direction': libagent.direction_names[action]
#        'direction': random.choice(libagent.direction_names)
    }

def main():

#    Timer calls to check turns don't last over 2 secs
#
#    starttime = time.time()
#    dt = time.time()-starttime
#    print("Turn took %g s"%(dt%60))
    
    if len(sys.argv) != 3:
        print("Usage: ./agent arena_host arena_port")
        exit(1)

    libagent.main(sys.argv[1], int(sys.argv[2]), "mutant-killer-bees", think)


main()
