#!/usr/bin/env python
# coding: utf-8

# In[1]:


10/0


# In[2]:


print(varx)


# In[3]:


lista = [5, 9, 10]


# In[4]:


lista[5]


# In[5]:


sum(lista)


# In[6]:


listb = []
try:
    res = sum(listb)/len(listb)
    print(res)
except NameError:
    print("listb not created")


# In[10]:


listb = []
try:
    res = sum(listb)/len(listb)
    print(res)
except NameError:
    print("listb not created")
except ZeroDivisionError:
    print("div by zero")


# In[11]:


listb = []
try:
    print(listb[4])
    res = sum(listb)/len(listb)
    print(res)
except NameError:
    print("listb not created")
except ZeroDivisionError:
    print("div by zero")


# In[12]:


listb = []
try:
    print(listb[4])
    res = sum(listb)/len(listb)
    print(res)
except NameError:
    print("listb not created")
except ZeroDivisionError:
    print("div by zero")
except :
    print("got caught at last")


# In[16]:


lista = [3, 7, 8, 9]
try:
    n = int(input("enter a positive integer"))
    if n < 0:
        raise ValueError("not a positive num")
    else:
        print(lista[n])
except ValueError as obj:
    print("type of obj is ", type(obj))
    print(obj)


# In[18]:


listb = []
try:
    try:
        pass
        pass
    except:
        pass
    
    print(listb[4])
    res = sum(listb)/len(listb)
    print(res)
except NameError:
    print("listb not created")
except ZeroDivisionError:
    print("div by zero")
except :
    print("got caught at last")


# In[25]:


lista = [3, 7, 8, 9]
try:
    try:
        n = int(input("enter a positive integer"))
        if n < 0:
                raise ValueError("not a positive num")
        else:
            print(lista[n])
    except ValueError as obj:
        print("type of obj is ", type(obj))
        print(obj)
        
except :
        print("outer except")


# In[27]:


class ErrorApp(Exception):
    "base class for errors in my app"
    pass

class SmallVal(ErrorApp):
    "too small"
    pass

class LargeVal(ErrorApp):
    """too large"""
    pass

num = 10

while True:
    try:
        i_num = int(input())
        if i_num < num:
            raise SmallVal
        elif i_num > num:
            raise LargeVal
        else:
            break
    except SmallVal:
        print(SmallVal.__doc__)        
    except LargeVal:
        print(LargeVal.__doc__)
print("guessed it right")


# In[ ]:




