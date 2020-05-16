import matplotlib.pyplot as plt
import csv
import sys
import os
import pandas as pd
import numpy as np
from collections import defaultdict

def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
		return i + 1

def roundTo5(x, base=5):
    return base * round(x/base)

# used to set the x axis to specific residue values
# residueNumber = [11,53,108,121,17,134,80,81,68, 145, 20, 34, 64] #2W3V
# residueNumber = [27,100,113,53,93,2,13,65,91,127] #1DG5/

# in order from smallest to largest
targetResidue = ["G", "A", "S", "C", "D", "P", "N", "T", "E", "V", "Q", "H", "M", "L", "I", "K", "R", "F", "Y", "W"]

if len(sys.argv) != 3:
	print("Usage: python plotEMpercent.py [file path] [threshold]\nthreshold can be a number {0, -3000} or percentage {50%, 95%}")
	sys.exit(0)

# where the plots will be stored
outputDir = "plotOutput/"
logDir = "plotOutputLog/"
if not os.path.exists(outputDir):
	os.makedirs(outputDir)
if not os.path.exists(logDir):
	os.makedirs(logDir)

dictionary = defaultdict(list)

# parse threshold
usingPercent = False
threshold = sys.argv[2]
if threshold[-1] == "%":
	usingPercent = True
	threshold = float(threshold[:-1]) / 100
else:
	threshold = float(threshold)

# parse file
path = sys.argv[1]
f_len = file_len(path) - 1
if "/" in path:
	title = path.split("/")[-1].split(".")[0] + "-stepsUntilLessThan(" + str(sys.argv[2]) + ")"
else:
	title = path.split(".")[0] + "-stepsUntilLessThan(" + str(sys.argv[2]) + ")"

# used for range of y axis
minCount = 1000
maxCount = 0

log = open(logDir + title + "log.csv", 'w')
logger = csv.writer(log)
logger.writerow(("resNum", "targetRes", "steps", "max", "min", "threshold", "em[2:]"))

for res in targetResidue:
	with open(path) as csvFile:
		reader = csv.reader(csvFile)
		next(csvFile) # reads headers

		for i in range (0,f_len):
			line = next(reader)
			if (line[2] == res):
				# reads em as floats and skips the first 2
				lst = list(line[-1].split(";")[2:])
				lst = [float(i) for i in lst]

				if usingPercent:
					lstMax = sys.maxsize * -1
					lstMin = sys.maxsize

					usingGlobal = 1
					if usingGlobal:
						#Min/Max being calculated globally
						for num in lst:
							if num < lstMin:
								lstMin = num
							if num > lstMax:
								lstMax = num
					else:
						#Min/Max being calculated from first and last
						lstMax = lst[0]
						lstMin = lst[-1]

					calculatedThreshold = lstMax - (threshold * (lstMax-lstMin))
				else:
					calculatedThreshold = threshold
					lstMax = "NA"
					lstMin = "NA"
				
				windowInitial = 5
				window = windowInitial
				count = 0
				for num in lst:
					if window == 0:
						count -= windowInitial
						break
					if num < calculatedThreshold:
						window -= 1
					else:
						window = windowInitial
					count += 1
				
				if count < minCount:
					minCount = count
				if count > maxCount:
					maxCount = count

				logger.writerow((line[1], res, count, lstMax, lstMin, round(calculatedThreshold, 4), lst))

				dictionary[res].append(int(count))


df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in dictionary.items() ]))
plot = df.boxplot()
# print(df)

maxCount = roundTo5(maxCount)
intervals = maxCount / 5
plt.yticks(np.arange(minCount,maxCount+2,intervals))

# labels
plt.ylabel("steps")
plt.xlabel("targetResidue")
plt.suptitle(title)
plt.grid(axis='x')

plt.savefig(outputDir + title + ".png")

