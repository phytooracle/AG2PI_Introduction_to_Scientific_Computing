import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-n','--number', type = int, help='a number')

args = parser.parse_args()


print('You can use any argmuent like: ', args.number) 
