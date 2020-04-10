import pandas as pd
import math
import os
import sys


def em_diff(filename):
    '''
    This method grabs em values from the em column
    and calculates the difference between start and end em
    
    :param filename: name of csv
    :return:
    '''

    data = pd.read_csv(filename, delimiter = ',')
    df = pd.DataFrame(data)
    
    em_split = df['em'].str.split(pat= ';')
    
    A1 = []
    
    # Iterates through rows and calcs em_diff and places it into a list
    for index, row in em_split.items():
        # If item has no em values, append nan
        if not isinstance(row, list) and math.isnan(row):
            A1.append(float("nan"))
            continue
        row_len = len(row)
        start_em = float(row[0])
        end_em = float(row[row_len-1])
        diff = end_em - start_em
        A1.append(diff)
        
    df.insert(11, "em_diff", A1, True)
    
    # Create directory
    outdir = './em_diff'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
        
    path_to_save = os.path.join(outdir, filename)
    
    #Save to path listed above
    df.to_csv(path_to_save, index=False)
    
# Only runs if this program is main
if __name__ == "__main__":
    if ((len(sys.argv) < 2 or len(sys.argv) > 2)):
        print ("arguments: [csv file name]")
        sys.exit(0)
    csv_name = sys.argv[1]
    em_diff(csv_name)