#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


dict1={
    "cgpa":['7.9','5.6','8.2','5.2','7.5','7.8','9.2','8.2'],
    "iq":['123','101','119','143','136','132','147','138'],
    "placement":['1','0','1','0','1','1','1','1']
}


# In[6]:


df=pd.DataFrame(dict1)


# In[8]:


df.head(5)


# In[9]:


df.shape


# In[10]:


df.size


# In[11]:


import matplotlib.pyplot as plt


# In[19]:


plt.scatter(df['iq'],df['cgpa'])


# In[13]:


plt.scatter(df['cgpa'],df['iq'],c=df['placement'])


# In[14]:


x=df.iloc[:,0:2]
y=df.iloc[:,-1]


# In[15]:


x


# In[16]:


y


# In[17]:


y.shape


# In[ ]:




