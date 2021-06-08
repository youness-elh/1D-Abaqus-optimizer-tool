import numpy as np
import os
import subprocess 
import time

directory = '//isi/w/elh' #'//isi/w/ditt'
script = 'Optimizer_tool/code/extraction_module'
script_path = os.path.join(directory,script)#'//isi/w/elh/Optimizer_tool/code/extraction_module.py'
comments_file = os.path.join(directory,'Optimizer_tool/state.txt')

#create the state file if not existing and write ('--------Waiting for signal to start extraction ...--------------')
with open(comments_file,'w+') as file:
	file.write('Waiting for signal to start extraction...')
	file.write('\n-----------end now------------')
print('\n ---------Waiting for signal to start extraction... ----------\n')

i=1
while True:
	time.sleep(10)
	oldfile = open(comments_file,'r+')
	text = oldfile.readlines()
	#print(str(text[-1]))
	if 'start now' in str(text[-1]):
		time.sleep(2)
		print('\n---------------Ongoing extraction of profiles for iteration: '+str(i)+'---------------- \n' )
		print('\t \t \t Check state.txt for details!!! \n')
		subprocess.call(['abq2019', 'viewer', 'noGUI='+str(script_path) ],shell=True)
		i+=1
		print('--------Waiting for signal to start new extraction ...--------------')
	oldfile.close()
		


		