import pandas as pd
import sys

if (len(sys.argv) < 2):
	print("Add path to a csv file\nExample paths:\n/research/jagodzinski/resilience_output/thomp276/2020-04-17-csvOutput/3TQ8.2001.out-1.csv\n../2020-04-17-csvOutput/3TQ8.2001.out-1.csv")
	sys.exit(0)

data = pd.read_csv(open(sys.argv[1]), keep_default_na=False)
# print(data)

if (len(sys.argv) < 4):
	print(data.corr())
	print("Add two columns as arguments to see more exact result")
	sys.exit(0)

print("\nPearson correlation of", sys.argv[2], "and", sys.argv[3])
try:
	print(data[sys.argv[2]].corr(data[sys.argv[3]]))
except:
	print("Could not run on this csv")