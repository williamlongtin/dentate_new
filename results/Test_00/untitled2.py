# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 20:59:00 2020

@author: mbezaire
"""

cells = dict()
with open('results/Test/celltype.dat') as f:
    cell_reader = csv.DictReader(f,delimiter=" ")
    for cell in cell_reader:
           cells.append(dict(cell))