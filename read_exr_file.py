import os
import argparse
from imageio import imread
from utils import read_h_planes, read_v_planes

def save_to_txt(filename, data):
    with open(filename, 'w') as f:
        for row in data:
            line = ' '.join(str(x) for x in row)
            f.write(f"{line}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--h_planes', required=True)
    parser.add_argument('--v_planes', required=True)
    parser.add_argument('--outdir', required=True)
    args = parser.parse_args()

    # Read input
    v_planes = imread(args.v_planes)
    h_planes = imread(args.h_planes)

    # Create the file name
    k = os.path.split(args.v_planes)[1][:-13]

    # Create full path for the .txt files
    v_planes_txt = os.path.join(args.outdir, f"{k}.v_planes.txt")
    h_planes_txt = os.path.join(args.outdir, f"{k}.h_planes.txt")

    # Save to .txt files
    save_to_txt(v_planes_txt, v_planes)
    save_to_txt(h_planes_txt, h_planes)