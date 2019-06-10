#!/usr/bin/env python
# coding: utf-8

# In[1]:


def funca():
    print("wake up srinidhi")


# In[2]:


funca()


# In[3]:


type(funca)


# In[11]:


def funcb(vara, varb):
    print(vara)
    print(varb)


# In[5]:


funcb(5, "hi")


# In[6]:


type(vara)


# In[7]:


varc = funcb(9,0)


# In[8]:


varc


# In[9]:


print(varc)


# In[12]:


def funcc(vara, varb):
    print(vara)
    print(varb)
    return 667


# In[13]:


varc = funcc(7, 8)


# In[14]:


print(varc)


# In[15]:


def funcd(vara, varb):
    print(vara)
    print(varb)
    return 667, 45 


# In[16]:


vard , vare = funcd(6,7)


# In[17]:


vard


# In[18]:


vare


# In[20]:


def funce(vara, varb):
    return 667, 45 , vara


# In[24]:


vare, varf = funce(6,7)


# In[22]:


type(vare)


# In[23]:


vare


# In[25]:


def funcf(vara = 23, varb = 11):
    print(vara)
    print(varb)
    return None


# In[26]:


funcf(3,2)


# In[27]:


funcf()


# In[28]:


funcf(6)


# In[29]:


def funcf(vara, varb = 11):
    print(vara)
    print(varb)
    return None


# In[30]:


funcf(7,9)


# In[31]:


funcf(7)


# In[34]:


def funcg(vara = 33, varb = 22):
    print(vara)
    print(varb)
    return None


# In[35]:


funcg(vara = 4)


# In[36]:


funcg(varb = 4)


# In[38]:


funcc(varb = 4, vara = 2)


# In[39]:


def funcg(vara = 33, varb = 22):
    print(vara)
    print(varb)
    return None


# In[41]:


funcg(7)


# In[54]:


def funch():
    print("in h")
    pass
    del funch
    def funci():
        print("in i")
        #some calculation
        return 7
    pass
    print("still in h")
    loca = funci()
    print("back in h")


# In[55]:


funch()


# In[46]:


def funcc(vara, varb):
    print(vara)
    print(varb)
    return 667


# In[48]:


print(funcc(7,8))


# In[56]:


def funch():
    print("in h")
    pass
    del funch
    def funci():
        print("in i")
        #some calculation
        return 7
    pass
    print("still in h")
    loca = funci()
    print("back in h")


# In[57]:


funch()


# In[58]:


def funch():
    """ to demonstrate 
    local function"""
    print("in h")
    pass
    del funch
    def funci():
        print("in i")
        #some calculation
        return 7
    pass
    print("still in h")
    loca = funci()
    print("back in h")


# In[59]:


print(funch.__doc__)


# In[60]:


print(funcc.__doc__)


# In[61]:


help(funch)


# In[62]:


listb = {'dhoni':'csk', 'kohli':'rcb', 'sharmaji':'mi', 'ashwin':'kxip'}


# In[63]:


listb


# In[64]:


listb['dhoni']


# In[65]:


listb['dhoni'] = 'rpg'


# In[66]:


listb


# In[67]:


listb['rahane'] = 'rr'


# In[68]:


listb


# In[69]:


tup1 = (5, 6, 'hi')


# In[70]:


dict1 = {tup1:"data1", 'cricket':listb}


# In[71]:


dict1['cricket']['ashwin'][1]


# In[72]:


import this


# In[73]:


seta = (5, 7, 0, 'hi', 10, 5, 0)


# In[74]:


seta


# In[75]:


seta = {5, 7, 0, 'hi', 10, 5, 0}


# In[76]:


seta


# In[77]:


seta[2]


# In[78]:


10 in seta


# In[80]:


setb = {7, 4, 10, 'hey'}


# In[81]:


seta 


# In[82]:


setb


# In[84]:


seta | setb


# In[85]:


setc = {}


# In[86]:


type(setc)


# In[89]:


tup2 = (2)


# In[90]:


type(tup2)


# In[92]:


tup2 =(2,)


# In[93]:


tup2 = 2,


# In[95]:


listd = list(tup1)


# In[96]:


listb.keys()


# In[97]:


list_keys = list(listb.keys())


# In[98]:


list_keys[2]


# In[99]:


type(list_keys)


# In[100]:


def funcx(*args):
    #print()
    for varx in args:
        print(varx)


# In[101]:


funcx("hi", "hello")


# In[102]:


funcx(6, 9, 10)


# In[103]:


def funcy(*args):
    print(args)
#    for varx in args:
#        print(varx)


# In[105]:


funcy(7,8)


# In[106]:


funcy([5,6,7],'hi', 8)


# In[ ]:




