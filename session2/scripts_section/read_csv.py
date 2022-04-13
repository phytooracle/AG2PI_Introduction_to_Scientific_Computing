import pandas as pd
import argparse

# Setup Arguments
parser = argparse.ArgumentParser(description='Process some integers.')

# parser.add_argment('-{command line character}', '--{variable in script}', type = {str, int, float}, help = 'a message to display')
parser.add_argument('-c','--csv', type = str, help='Path to a csv')

args = parser.parse_args()
# -----------------------------------------------------------------------------------------

# Example from notebook
df = pd.read_csv(args.csv)

print(df.head())