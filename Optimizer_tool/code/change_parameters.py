import numpy as np
import math
import sys
import os
import re
import shutil #deleting a directory
from numpy import savetxt
import time
import matplotlib.pyplot as plt
import sys

start_time = time.time()

###########################################################
################## Parameters to set ######################
###########################################################
directory = '//isi/w/elh/Optimizer_tool/test'#'//isi/w/ditt/Optimizer_tool/test'
param_line = 27
modify_file= os.path.join(directory,'DFLUX_21L_R60_t15_L19.f') #file to modify
new_par = float(sys.argv[1])
######################################################################
##################### open file and read lines  ######################
######################################################################
oldfile = open(modify_file,'r')
text = oldfile.readlines()
#print(text[27])#line of the parameter to change QT = 1.6*14.0e3
######################################################################
##################### modify the old parameters  #####################
######################################################################
if 'QT' in text[param_line]:
    old = text[param_line]
    text[param_line] = '\t \t QT = '+str(new_par)+" \n"
else: 
    print("Given line of the parameter QT is not detected")

newfile = open(modify_file,'w')
text = newfile.writelines(text)
print("\n"+str(old)+ "\t \t become: "+str(new_par))


end_time = time.time()
elapsed_time = end_time - start_time 
#print("Elapsed time to update the parameters "+str(elapsed_time)+" seconds")


