from pkg_resources import Environment
import gym
from stable_baselines3.common.env_checker import check_env
#from stable_baselines3 import DQN
from stable_baselines3.dqn.policies import MlpPolicy
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO


#if path does not work try this instead
import sys
sys.path.append("bee-arena/gym_basic/envs")
from basic_env import BasicEnv
from bee_arena import BeeArena

env = BasicEnv()

#env = gym.make("gym_basic:basic-v0")

check_env(env)

#bee_arena_env = gym.make("gym_basic:bee-arena-v0")

bee_arena_env = BeeArena()

check_env(bee_arena_env)

print("Bee Arena Environment loaded")


model = PPO("MlpPolicy", bee_arena_env, verbose=1)
model.learn(total_timesteps=10000)

model.save("MKB1s")

obs = env.reset()
for i in range(10):
    action, _states = model.predict(obs)
    print(action)
    obs, reward, dones, info = env.step(action)
    env.render()
