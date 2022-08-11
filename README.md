# vqgan-auto-batch
Script to automate the generation of multiple images from VQGAN-CLIP

<img src=./img/3bp.png width=200>
 <img src=./img/3bp1.png width=200>
 <img src=./img/3bp2.png width=200>
 <img src=./img/3bp3.png width=200>
 <img src=./img/3bp4.png width=200>

## Requirements:

Install the nerdyrodent implementation of VQGAN-CLIP for PyTorch: from https://github.com/nerdyrodent/VQGAN-CLIP

Doing this install will set you up with all the requirements and dependencies.

## To run:

### .sh script:

Create a prompt of your choosing. You can modify the example in `threebody.sh`:

`a painting of three suns orbs rotating in sky | dystopian | physics alpha centauri | trending artstation`

Pass an argument for the `--output` file and based on the nerdyrodent `generate.py`, the `--conf` and `--ckpt` (configuration, checkpoint).

This script requires GPU.

### .py script:

The `.sh` script is hard-coded into the `.py` script (line 16), like so:

`s = subprocess.check_output('./threebody.sh -f %s -g %s' % (var, gpu), shell = True)`

Simply change to your bash script name. Pass an argument for the number file you want to start with and then (end) how many you want to generate.

Run:

```
python automake_nft.py --start 1 --end 20

```
