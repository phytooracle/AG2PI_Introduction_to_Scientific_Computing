import argparse

# Setup Arguments
parser = argparse.ArgumentParser(description='Process some integers.')

# parser.add_argment('-{short flag}', 
#                    '--{short flag}', 
#                      type = {str, int, float}, 
#                       help = 'a message to display')

parser.add_argument('-n',
                    '--name', 
                    type = str, 
                    help='a name')

args = parser.parse_args()

#------------------------------------------------------------------------------------------------------------------------------------ 

print('Hello', args.name) 
