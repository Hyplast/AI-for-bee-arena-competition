Mutant Killer Bees -Agent
====================

## Requirements

- Python 3.9
- PyTorch 1.81
- Gym (0.19.0)
- Stable_baselines3 (1.4)

## How to use

# windows
# install PyTorch (if you have CUDA = Nvidia GPU, you can install CUDA version instead of CPU version)
# pip3 install torch==1.11.0+cpu torchvision==0.12.0+cpu torchaudio===0.11.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

1. Install pip install gym=0.19.0
2. pip install stable-baselines3 [on Mac- brew install cmake openmpi] 
3. Install the gym enviroment. pip install -e gym-basic

MTB.zip contains trained RL model. To train a new model run "train.py"


The `libagent.py` module mirrors closely the original C version, with the following adjustments for the language:

- structs become Python dictionaries
- C constants become strings
- In the `agent_info` dictionary, the `cells` field is a dictionary of dictionaries, and uses indices relative to the bee's position. That is, the bee is at `[0][0]`, and indices range from `-VIEW_DISTANCE` to `VIEW_DISTANCE`
