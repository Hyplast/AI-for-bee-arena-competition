import gym
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import DQN
from stable_baselines3.dqn.policies import MlpPolicy
from stable_baselines3.common.vec_env import DummyVecEnv

env = gym.make("gym_basic:basic-v0")

check_env(env)

#bee_arena_env = gym.make("gym_basic:bee-arena-v0")

#check_env(bee_arena_env)

model = DQN("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)

model.save("MTB")

obs = env.reset()
for i in range(10):
    action, _states = model.predict(obs)
    print(action)
    obs, reward, dones, info = env.step(action)
    env.render()
