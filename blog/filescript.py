import pandas as pd
def handle_uploaded_file(f):
    for line in f:
    	listR=[line.rstrip() for line in f]
    	#listR=[line.split('\t') for line in listR]
    	#by_col=zip(*list_of_list)
    	#gg=by_col[2][1:10]
    	#gg=[float(el) for el in gg]
    	sub=listR
    	return sub

def handle_csv_file(f):
    df=pd.read_csv(f)
    Name=df['Geneid']
    Length=df['Length']
    geneName= (Name,Length)
    return geneName
