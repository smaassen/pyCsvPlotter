
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

use_data_for_x = False
items_to_plot=[]
x_key='-1'
i_delimiter=';'
file_name=''

#####################################
# Parsing arguments
#####################################

if (len(sys.argv)<2):
    print('Error: specify at least the file location:')
    print('   ex: $ python ', sys.argv[0], ' myfile.csv')
    sys.exit()

if (len(sys.argv) == 2):
    file_name = sys.argv[1]

if (len(sys.argv)>2):
    file_name = sys.argv[1]
    if('axis=' in sys.argv[2]):
        # Plot against given variable
        x_key = sys.argv[2][5:]
        print('Axis defined as', x_key)
        use_data_for_x = True
    else:
        items_to_plot.append(sys.argv[2])
    
    if (len(sys.argv)>3):
        #plot only requested variables
        for i in range(3,len(sys.argv)):
            items_to_plot.append(sys.argv[i])
            
# User information 
if len(items_to_plot)>0:
    print("Items selected to plot ", items_to_plot)
else:
    print("Plotting all items ")
    
    
with open(file_name) as csvfile:
    
    #####################################
    # Reading file
    #####################################
    
    reader = csv.DictReader(csvfile, delimiter=i_delimiter)
    keys=next(reader).keys()
    data = []
    csvfile.seek(0)
    next(reader)
    i=0;
    for row in reader:
        #data[:,i] = float(list(row.values()))
        data.append(list(row.values()))
        i=i+1
        
    a=np.array(data)
    keylist=list(keys) 
    
    #####################################
    # Finding relevant indicies
    #####################################
    
    x_ind={}
    y_ind={}
    for key in keylist:
        if (key==x_key):
            x_ind.update({key:keylist.index(key)})
        else:
            if (len(items_to_plot)>0):
                if (key in items_to_plot):
                    y_ind.update({key:keylist.index(key)})
            else:
                y_ind.update({key:keylist.index(key)})
    
    #####################################
    # Plotting
    #####################################
    
    s=a.shape[0]
    for y_key, y_ind_val in y_ind.items():
        if use_data_for_x:
            plt.plot(a[:,x_ind[x_key]], a[:,y_ind_val],label=y_key)
        else:
            plt.plot(np.arange(0,s),a[:,y_ind_val],label=y_key)
                
    plt.legend()
    plt.show()

    
    
