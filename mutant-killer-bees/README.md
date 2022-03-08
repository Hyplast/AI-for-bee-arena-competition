Mutant Killer Bees -Agent
====================

## Requirements

- Python 3.9.10
- Gym (0.19.0)
(- Cloudpickle (1.6.0) )
- Stable_baselines3 (1.4.0)

## How to use

1. Install pip install gym
2. pip install stable-baselines3 [on Mac- brew install cmake openmpi]
3. Install the gym enviroment. pip install -e gym-basic

MTB.zip contains trained RL model. To train a new model run "train.py"


The `libagent.py` module mirrors closely the original C version, with the following adjustments for the language:

- structs become Python dictionaries
- C constants become strings
- In the `agent_info` dictionary, the `cells` field is a dictionary of dictionaries, and uses indices relative to the bee's position. That is, the bee is at `[0][0]`, and indices range from `-VIEW_DISTANCE` to `VIEW_DISTANCE`
