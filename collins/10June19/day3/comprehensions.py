#!/usr/bin/env python
# coding: utf-8

# In[1]:


lista = []


# In[2]:


for var in 'friends':
    lista.append(var)


# In[3]:


lista


# In[4]:


listb = [var for var in 'friends']


# In[5]:


listb


# In[6]:


lista == listb


# In[10]:


listc = [x for x in range(6)]


# In[8]:


listc


# In[11]:


listd = [x for x in range(9) if x%2 == 0 ]


# In[12]:


listd


# In[13]:


listx = [1,2,3,4]
listy = [2,3,4,5]
list_common = []


# In[14]:


for valx in listx:
    for valy in listy:
        if valx == valy:
            list_common.append(valx)


# In[15]:


list_common


# In[16]:


list_com = [valx for valx in listx for valy in listy if valx == valy ]


# In[17]:


list_com


# In[18]:


num = [1,2,34]

varx = 3
varx**2


# In[19]:


num = [1,2,34]
square = [n**2 for n in num]


# In[20]:


square


# In[23]:


def funca(arr):
    res = []
    for i in arr:
        res.append(i**2)
    return res


# In[24]:


get_ipython().run_line_magic('timeit', 'funca(range(1, 12))')


# In[25]:


def funcb(arr):
    return [i**2 for i in arr]


# In[26]:


get_ipython().run_line_magic('timeit', 'funcb(range(1, 12))')


# In[27]:


"""
^a..a$ 
asia 
area
america
asss
"""


# In[28]:


import re


# In[30]:


pattern = '^a..a$'
string = input()
res = re.match(pattern, string)
if res:
    print("found a match")
else:
    print("no match")


# In[3]:


import re
patterna = 'h..l'
patternb = 'h..l$'
string = input()
res = re.findall(patternb, string)
if res:
    print(res)
else:
    print("no match")


# In[13]:


res = re.search("\"", "\thi are you high")


# In[14]:


res


# In[7]:


print(res)


# In[8]:


type(res)


# In[21]:


res = re.search(r"\\", r"\t hi are you high")


# In[22]:


res


# In[23]:


print("hi\n")


# In[24]:


print(r"hi\n")


# In[ ]:




