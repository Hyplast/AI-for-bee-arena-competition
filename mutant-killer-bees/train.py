import gym
from stable_baselines3.common.env_checker import check_env

env = gym.make("gym_basic:basic-v0")

check_env(env)

