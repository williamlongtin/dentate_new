# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:59:00 2020

@author: mbezaire
"""
import csv 

cell_ranges = {}
with open('results/Test_06/celltype.dat') as f:
    cell_reader = csv.DictReader(f,delimiter="\t")
    for cell in cell_reader:
        cell_ranges[cell["celltype"]] = range(int(cell["rangeStart"]),int(cell["rangeEnd"])+1)

