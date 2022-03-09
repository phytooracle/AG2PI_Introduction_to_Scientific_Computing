import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-n','--number', type = int, help='a number')

args = parser.parse_args()


print('You entered', args.number)
print('Your number plus 10 is:', args.number + 10)
