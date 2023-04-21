#!/usr/bin/env python
# coding: utf-8

# # welcome to numpy tutorial

# In[5]:


import numpy as np


# In[6]:


listarray = np.array([[1,2,3],[5,8,5],[2,3,1]])


# In[7]:


listarray


# In[8]:


listarray.size


# In[9]:


listarray.shape


# In[10]:


lspace = np.linspace(1,50,10)


# In[11]:


lspace


# In[12]:


ide = np.identity(45)


# In[13]:


ide


# In[14]:


arr=np.arange(99)


# In[15]:


arr


# In[16]:


arr.reshape(3,33)


# In[17]:


x=[[1,2,3],[4,5,6],[2,4,5]]


# In[21]:


ar=np.array(x)


# In[22]:


ar


# In[23]:


ar.sum(axis=0)


# In[24]:


ar.sum(axis=1)


# In[26]:


ar.flat


# In[28]:


for item in ar.flat:
    print(item)


# In[29]:


ar.nbytes


# In[30]:


one=np.array([1,3,4,98,76,64,2])


# In[31]:


one.argsort()


# In[32]:


ar


# In[34]:


ar.argsort()


# In[35]:


ar.ravel()


# In[36]:


ar2=np.array([[1,4,3]
             ,[2,4,7],
             [5,6,7]])


# In[37]:


ar+ar2


# In[50]:


ar*ar2


# In[39]:


np.nonzero(ar)


# In[40]:


import sys


# In[41]:


py_ar=[0,4,55,2]


# In[42]:


np_ar=np.array(py_ar)


# In[43]:


sys.getsizeof(1)*len(py_ar)


# In[ ]:




