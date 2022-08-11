import subprocess
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--start", type=int, default=1, help="start file")
parser.add_argument("--end", type=int, default=20, help="end file")
parser.add_argument("--gpu", type=int, default=0, help="gpu_num")
opt = parser.parse_args()
print(opt)


def make_nft(start, end, gpu):
    for i in range(start, end):
        var = str(i) 
        s = subprocess.check_output('./threebody.sh -f %s -g %s' % (var, gpu), shell = True)
        print(i)
        

if __name__ == '__main__':
    
    # set permissions
    os.system('chmod 755 -R threebody.sh')

    make_nft(opt.start, opt.end, opt.gpu)