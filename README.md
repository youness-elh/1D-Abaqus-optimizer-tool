# 1D-Abaqus-optimizer-tool
This tool is provided to Abaqus users in welding applications in order to automate the pre-processing, the processing and the post-processing in a loop until the key parameter is identified using a gradient descent method. This work is a preparation for the master thesis .

## Road-map:
**Parameters control of a heat source model in Abaqus welding simulations**

## Heat source model
### Parameters of control
The heat source model is based on the Goldak model and has *5 key parameter*:
* Q: the heat source maximum intensity,
* Af: Front length of the molten zone
* Ar: Rear length of the molten zone
* B:Half of the width of the bead
* C: Penetration of the bead

 In order to familiarize with the topic, only Q is considered as an optimization parameter within this work. The other parameters are fixed.
### Target function
In order to find the optimal parameter Q, one should define an objective function based on one of the following inputs:
  *  2D or 3D *Images*
  *  *Measurements* over the welding simulated model

## Abaqus welding simulations
### Pre-processing scripts
The purpose is running automatically a number of simulations given predefined parameters. The parameters are found in the input file and are modified based on a *python script*. The material model file is also required to run the main script launching the job on the computation server.
### Post-processing scripts
Once the simulation is done, a *post-processing script* has the task to extract the predefined measures of temperature according to the target function variable.

## References

This work is done in Fraunhofer IWM at the Structural Integrity and Fracture Mechanics group under the supervision of Mr. Florian Dittmann and Mr. Igor Varfolomeev.
