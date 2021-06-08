This instance is running with the following parameters:
penalty=1e-30
direction= step*np.sign(gradient)
step = 18000
	if iter == 1:
		step = 200

max iter = 30
	max iter = 30
----------------------------------------
	-----------How to use:----------
----------------------------------------
0/ Copy the folder Optimizer_tool to //isi/w/USR/ (e.g //isi/w/elh)
1/ On your windows command prompt locate on C:/Users/[elh] and run ------> python w:Optimizer_tool\code\Extract_profiles.py
2/ Then login to the hpc cluster and locate in: //isi/w/USR/Optimizer_tool/test (e.g //isi/w/elh/Optimizer_tool/test)
4/ Finally run ---------------------------------> python ../code/Optimizer.py


----------------------------------------
  -----How to check results:----------
----------------------------------------
1/ relevant outputs on the 'result' folder 
2/ figures on the 'plot' folder
3/ temperature profile on the 'T_t_extraction.txt'

Note:
1/ The odb should be compatible with abaqus 2019 version
2/ The state of the script is given by 'state.txt'