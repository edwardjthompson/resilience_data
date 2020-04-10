import pandas as pd
import sys
import os


def normalize(filename, column_name):
    '''
    This method normalizes a column and places the normalized values
    one column to the right of the original
    
    :param filename: name of csv file
    :param column_name: column that should be normalized
    :return:
    '''
    try:
        data = pd.read_csv(filename, delimiter=',')
    except IOError as e:
        print(e)
        return
    df = pd.DataFrame(data)
    
    column_min = df[column_name].min()
    column_max = df[column_name].max()
    column_index = df.columns.get_loc(column_name)
    new_column_name = "normalized_" + column_name   
    
    df.insert(column_index+1, new_column_name, True)
    
    df[new_column_name]=(df[column_name]-column_min)/(column_max-column_min)
    
    #Creates a new directory to store results
    outdir = './result'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    
    path_to_save = os.path.join(outdir, filename)
    
    #Save to path listed above
    df.to_csv(path_to_save, index=False)

# Only runs if this program is main
if __name__ == "__main__":
    if ((len(sys.argv) < 3 or len(sys.argv) > 3)):
        print ("arguments: [csv file name] [column name]")
        sys.exit(0)
    csv_name = sys.argv[1]
    column_name = sys.argv[2]
    normalize(csv_name, column_name)