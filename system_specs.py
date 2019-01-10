#!/usr/bin/env python
# coding: utf-8

# In[1]:


from __future__ import print_function
import platform
import numpy as np
import multiprocessing
import subprocess
import psutil


# In[2]:


gpu_info = None
try:
    print('Fetching GPU info if it exists. This could take 1 minute.')
    gpu_info = subprocess.check_output('nvidia-smi')
except:
    pass


# In[3]:


print()
print('----------------')
print('| SYSTEM SPECS |')
print('----------------')
print('\nOS:', platform.system(), platform.version())
print('Architecture:', platform.architecture()[0], ",", platform.machine())
print('Storage:', int(round(psutil.disk_usage('/').total / (1024.0 ** 3))), 'GB')
print('RAM:', int(np.round(psutil.virtual_memory()._asdict()['available'] / 1e9, 0)), 'GB')
print('Num CPU:', multiprocessing.cpu_count())
if gpu_info is not None and len(gpu_info) > 0:    
    print('Num GPU:', str(gpu_info).count('W / '))
    print('\nGPU Information\n***************')
    print(gpu_info.decode())

