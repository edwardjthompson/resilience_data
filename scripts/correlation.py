import pandas as pd
import sys

data = pd.read_csv(open(sys.argv[1]), keep_default_na=False)
# print(data)

if (len(sys.argv) < 2):
	print("Add path to a csv file")
	sys.exit(0)

if (len(sys.argv) < 4):
	print(data.corr())
	print("Add two columns as arguments to see more exact result")
	sys.exit(0)

print("\nPearson correlation of", sys.argv[2], "and", sys.argv[3])

print(data[sys.argv[2]].corr(data[sys.argv[3]]))