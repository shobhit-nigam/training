#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[2]:


print("hi")
time.sleep(4)
print("woke up")


# In[3]:


class time_a:
    h = 0
    m = 0
    def __init__(self, hours =0, minutes =0):
        self.h = hours
        self.m = minutes
    


# In[18]:


obja = time_a(1, 40) 


# In[19]:


objb = time_a(1, 50) 


# In[20]:


objc = time_a()


# In[21]:


objc = obja + objb


# In[17]:


class time_a:
    hours = 0
    minutes = 0
    def __init__(self, h =0, m =0):
        self.hours = h
        self.minutes = m
    def __add__(self, selfb):
        total = time_a()
        temp1 = self.hours * 60 + self.minutes
        temp2 = selfb.hours * 60 + selfb.minutes
        temp3 = temp1 + temp2
        total.hours = temp3//60
        total.minutes = temp3%60
        return total


# In[22]:


objc = obja + objb


# In[23]:


objc.hours


# In[24]:


objc.minutes


# In[25]:


obcd = obja + objb + objc


# In[26]:


obcd.hours


# In[27]:


obcd.minutes


# In[28]:


class sonia:
    def __init__(self):
        print("in init of sonia")
    def bold(self):
        print("beautiful")


# In[29]:


objs = sonia()


# In[34]:


class rahul(sonia):
    def strong(self):
        print("rafael")


# In[35]:


objr = rahul()


# In[36]:


objr.bold()


# In[37]:


objr.strong()


# In[40]:


class priyanka(sonia):
    def __init__(self):
        print("in init of priyanka")
    def strong(self):
        print("rafael")


# In[51]:


objp = priyanka()


# In[50]:


class priyanka(sonia):
    def __init__(self):
        sonia.__init__("hey")
        print("in init of priyanka")
    def strong(self):
        print("rafael")


# In[56]:


def funcd(**kwargs):
    for key, val in kwargs.items():
        print(key, ': \t', val)


# In[57]:


funcd(x = 20, y = 30, z = 40)


# In[58]:


la = [8, 9, 12]


# In[59]:


lb = ['e', 'y', 'd']


# In[60]:


z = zip(la, lb)


# In[61]:


type(z)


# In[62]:


z


# In[63]:


res = set(z)


# In[64]:


res


# In[65]:


z


# In[66]:


res_l = list(z)


# In[67]:


res_l


# In[68]:


z = zip(la, lb)
res_l = list(z)


# In[69]:


res_l


# In[70]:


z = zip(la, lb)
res_l = dict(z)


# In[71]:


res_l


# In[72]:


res_l[12]


# In[73]:


import os


# In[74]:


os.getcwd()


# In[77]:


os.listdir()


# In[78]:


import sys


# In[79]:


sys.path


# In[80]:


type(sys.path)


# In[81]:


import imp


# In[82]:


imp.load_source('yy', 'C:\\Users\\bsunkara\\Desktop\\python training\\day1\\sample.py')


# In[83]:


import yy


# In[84]:


yy.funcs()


# In[ ]:




