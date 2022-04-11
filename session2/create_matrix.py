import argparse
# Import Numpy as alias 'np'
import numpy as np

parser = argparse.ArgumentParser(description='Create a matrix')
parser.add_argument('-x','--x_size', type = int, help='a number')
parser.add_argument('-y','--y_size', type = int, help='a number')

args = parser.parse_args()

# create a matrix (2 dimensional array) with size 4 by 6 with all elements equal to one
matrix = np.ones(((args.x_size, args.y_size)))
print("Matrix: \n", matrix)
