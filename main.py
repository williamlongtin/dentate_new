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
h('Scale = 20000') # How many real cells are represented by one
                 # model cell (so larger numbers mean smaller models)
                 # 20000 - good for making sure code can run, may take
                 # 2 - 8 min
                 # 2000 or 1000 - better for more realistic results
                 # but may take a long time depending on your computer
#%%
h.RunName = "Test"
h.PercentCellDeath = 50
h.PercentAxonSprouting = 50
h.SimDuration = 2000
pc = h.ParallelContext()
# check if dir exists
# update RunName if necessary
if (pc.id()==0):
    while (os.path.exists("results/"+h.RunName)):
        st=h.RunName.find("_")
        if (st>-1 and h.RunName[st+1:].isdigit()):
            b='{:0'+str(len(h.RunName[st+1:]))+'d}'
            h.RunName = h.RunName[:st+1] + b.format(int(h.RunName[st+1:])+1)
        else:
            h.RunName += '_00'
    
    #%%        
    os.mkdir("results/"+h.RunName)
pc.barrier()
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
        cell_ranges[cell["celltype"]] = [int(cell["rangeStart"]),int(cell["rangeEnd"])+1]


#%%
import numpy as np
import matplotlib.pyplot as plt

plt.figure()

mydata = np.loadtxt('results/'+ROI+'/spikeraster.dat')
#plt.scatter(mydata[:,0],mydata[:,1],s=.01)
#plt.ylabel("Cell #")

# Plotting interspersed cells in different colors by cell type:
pt_colors=[np.array([1,1,0]),np.array([.2,.2,.2]),np.array([1,0,0]),np.array([0,1,0]),np.array([0,0,1])]
#pt_colors=[np.array([1,1,0]),np.array([.2,0,.4]),np.array([1,.5,0]),np.array([.2,1,.9]),np.array([.8,.5,.8])]
pt_c=0
for key in cell_ranges:
    tmpdata = mydata[(mydata[:,1]>=cell_ranges[key][0]) & (mydata[:,1]<cell_ranges[key][1])]
    plotpos = (tmpdata[:,1] - cell_ranges[key][0])/(cell_ranges[key][1]-cell_ranges[key][0])*1000
    if (len(plotpos)==1 and plotpos[0]==0):
        plt.scatter(tmpdata[:,0],plotpos,s=20,c=pt_colors[pt_c].reshape(1,-1),label=key)
    elif (len(plotpos)/len(mydata)<.5):
        plt.scatter(tmpdata[:,0],plotpos,s=4,c=pt_colors[pt_c].reshape(1,-1),label=key)
    else:
        plt.scatter(tmpdata[:,0],plotpos,s=.05,c=pt_colors[pt_c].reshape(1,-1),label=key)
    pt_c += 1
    

plt.title("{} with Cell Death: {}%, Sprouting: {}%".format(ROI, PercentCellDeath,PercentAxonSprouting))
plt.xlabel("Time (ms)")
plt.ylabel("Cells (positioned)")
plt.legend(loc="upper left",fontsize=8)
#plt.xlim([200, 300])
plt.show()