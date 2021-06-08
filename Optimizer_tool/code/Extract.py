import numpy as np
import os
import subprocess 
import time


############################################################
#################### inputs ################################
#############################################################
directory = '//isi/w/elh'#'//isi/w/ditt'

#odb files
inp_file_name = 'Optimizer_tool/test/21L_R60_t15_3d_L19_heat.inp'
f_file_name = 'Optimizer_tool/test/DFLUX_21L_R60_t15_L19.f'
f_file = os.path.join(directory,f_file_name)
inp_file = os.path.join(directory,inp_file_name)

#file having the state of the odb model
state_odb_name = 'Optimizer_tool/test/21L_R60_t15_3d_L19_heat.sta'
state_odb = os.path.join(directory,state_odb_name)

#file having the state of the extraction process
state_file_name = 'Optimizer_tool/state.txt'
state_file = os.path.join(directory,state_file_name)

odb_dir = 'Optimizer_tool/test'
path_odb_dir = os.path.join(directory,odb_dir)



############################################################
#################### functionss ############################
#############################################################

def clean_files(t=1):
	files = [i for i in os.listdir(path_odb_dir) if i not in ('21L_R60_t15_3d_L19_heat.inp', 'DFLUX_21L_R60_t15_L19.f', 'WSModell_Kinematic_new.ssc','21L_R60_t15_3d_heat.fem')]#'21L_R60_t15_3d_L19_heat.odb','21L_R60_t15_3d_L19_heat.sta',
	#print(i)
	subprocess.call(['rm','-rf'] + files)
	time.sleep(t)
	

def exist(state_path):
	return os.path.exists(state_path)

def wait_step(state,keyword='SUCCESSFULLY',t=10):
	while not exist(state):
		print('Waiting for odb.sta to appear!')
		time.sleep(100)
		
	file = open(state,'r')
	text = file.readlines()
	file.close()
	
	while (len(text) < 2):
		print('Waiting more time!!')
		time.sleep(5)
		file = open(state,'r')
		text = file.readlines()
		file.close()
		
	last_line = text[-1]
	while keyword not in last_line:
		
		time.sleep(t)
		#print('last_line',last_line)
		while (len(text) < 2):
			print('Waiting more time!!')
			time.sleep(5)

		file = open(state,'r')
		text = file.readlines()
		file.close()
		last_line = text[-1]
			
		if keyword == 'SUCCESSFULLY':
			print('------------waiting for odb--------------')
			time.sleep(180)
		elif keyword == 'end now':
			print('waiting for extracted data')
			time.sleep(10)
		file.close()
	time.sleep(t)
	if keyword == 'SUCCESSFULLY':
			print('--------Ready to start extraction!-------')
	elif keyword == 'end now':
			print('\n \n------Extracted PROFILES are ready!------')			

##########################################################
#################### call ################################
##########################################################

	
#while True:
#calculate grad then Q 
# then Tsim then loss
wait_step(state_file,'end now',5)
#print('odb: write on odb.sta')
print('---------Clean old job outputs----------')
clean_files(2)
print('----------------------------------------')
print('-------------Run abaqus job-------------')
print('----------------------------------------')
subprocess.call(['abaqus_2019 -j 21L_R60_t15_3d_L19_heat -cpus 8 user=DFLUX_21L_R60_t15_L19'], shell=True)
# wait for odb
#extraction
wait_step(state_odb,'SUCCESSFULLY',5)
print('--------Extraction: starting now--------')
with open(state_file,'a') as file:
	file.write("\n -----------------Extraction: start now----------------")
	time.sleep(1)




