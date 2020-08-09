# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 19:07:08 2020

@author: mbezaire
"""


from neuron import h
import os
h('strdef RunName')
h('PercentCellDeath = 0') # % of vulnerable interneurons to remove
h('PercentAxonSprouting = 0') # % of extra connectivity allowed
h('SimDuration = 100') # duration of simulation in milliseconds
h('Scale = 1000') # How many real cells are represented by one
                 # model cell (so larger numbers mean smaller models)
#%%
h.RunName = "Test"
h.PercentCellDeath = 40
h.PercentAxonSprouting = 40
h.SimDuration = 1000
# check if dir exists
# update RunName if necessary
while (os.path.exists("results/"+h.RunName)):
    st=h.RunName.find("_")
    if (st>-1 and h.RunName[st+1:].isdigit()):
        b='{:0'+str(len(h.RunName[st+1:]))+'d}'
        h.RunName = h.RunName[:st+1] + b.format(int(h.RunName[st+1:])+1)
    else:
        h.RunName += '_00'

#%%        
os.mkdir("results/"+h.RunName)

h.load_file(1,"model-2.3.hoc")
h.pc.gid_clear()

print("This simulation is called: " + h.RunName)

ROI = h.RunName
PercentCellDeath = h.PercentCellDeath
PercentAxonSprouting = h.PercentAxonSprouting
#%%
import csv 

cell_ranges = {}
with open('results/'+ROI+'/celltype.dat') as f:
    cell_reader = csv.DictReader(f,delimiter="\t")
    for cell in cell_reader:
        cell_ranges[cell["celltype"]] = range(int(cell["rangeStart"]),int(cell["rangeEnd"])+1)


#%%
import numpy as np
import matplotlib.pyplot as plt

mydata = np.loadtxt('results/'+ROI+'/spikeraster.dat')

#for key in cell_ranges:
#    mydata[mydata[:,1] in cell_ranges[key]]


plt.figure()
plt.scatter(mydata[:,0],mydata[:,1],s=.01)
plt.title("{} with Cell Death: {}%, Sprouting: {}%".format(ROI, PercentCellDeath,PercentAxonSprouting))
plt.xlabel("Time (ms)")
plt.ylabel("Cell #")
plt.show()