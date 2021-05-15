# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:31:06 2021

@author: Null
"""

import os
import shutil


# Reset Files
if os.path.isdir('raw/'):
    shutil.rmtree('raw/')

if os.path.isdir('aligned/'):
    shutil.rmtree('aligned/')

if os.path.isdir('generated/'):
    shutil.rmtree('generated/')
    
try:
    os.mkdir('raw/')
    os.mkdir('aligned/')
    os.mkdir('generated/')
except:
    pass

