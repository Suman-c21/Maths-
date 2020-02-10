#!/usr/bin/env python
# coding: utf-8

# In[1]:


myfile = open('data.dat','w')
for i in range(1,11,1):
    i2 = i**2
    print >> myfile, '%1.1f \t %1.1f'%(i,i2)
myfile.close()


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
v0 = 30
g = 10
adeg = np.arange(15,75,10)
arad = adeg*(np.pi)/180
for angle in arad:
    tflg = ((2*v0)*np.sin(angle))/g
    t = tflg*np.linspace(0,1,100)
    x = v0*np.cos(angle)*t
    y = v0*np.sin(angle)*t - 0.5*g*t**2
    plt.plot(x,y)


# In[ ]:




