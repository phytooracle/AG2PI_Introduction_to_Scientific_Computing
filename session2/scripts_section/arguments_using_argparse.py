import argparse

# Setup Arguments
parser = argparse.ArgumentParser(description='Process some integers.')

# parser.add_argment('-{command line character}', '--{variable in script}', type = {str, int, float}, help = 'a message to display')
parser.add_argument('-n','--number', type = int, help='a number')

args = parser.parse_args()

#------------------------------------------------------------------------------------------------------------------------------------ 

print('You can use any argmuent like: ', args.number) 
