#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('save', 'tt 10-20')


# In[3]:


get_ipython().run_line_magic('lsmagic', '')


# In[4]:


get_ipython().run_line_magic('history', '-f tt.py')


# In[6]:


get_ipython().run_line_magic('ls', '')


# In[7]:


print "hey \n"


# In[10]:


get_ipython().run_cell_magic('ruby', '', 'print "hey \\n"')


# In[11]:


varx = 20


# In[12]:


varx = input()


# In[13]:


type(varx)


# In[14]:


vary = input()


# In[15]:


type(vary)


# In[16]:


vary = int(input())


# In[17]:


type(vary)


# In[18]:


varz = eval("456")


# In[19]:


type(varz)


# In[20]:


varu = eval(input())


# In[21]:


type(varu)


# In[22]:


varv = eval(input())


# In[23]:


type(varv)


# In[24]:


varv


# In[26]:


vars = input()


# In[29]:


help(vars)


# In[28]:


del vars


# In[30]:


class batman:
    power = ['rich', 'wings', 'genius']
    def fly():
        print("batman can fly")
    dataa = 3


# In[31]:


batman.power[1]


# In[33]:


batman.fly()


# In[34]:


class batman:
    power = ['rich', 'wings', 'genius']
    def fly():
        print("batman can fly")
    dataa = 3
    gf = 'rachel'


# In[35]:


varx = int()


# In[36]:


varx


# In[41]:


obja = batman()
#batman obja 


# In[38]:


#obja = batman()


# In[39]:


obja.fly()


# In[40]:


class batman:
    power = ['rich', 'wings', 'genius']
    def fly(ttt):
        print("batman can fly")
    dataa = 3
    gf = 'rachel'


# In[42]:


obja.fly()


# In[44]:


batman.fly("hello")


# In[45]:


class batman:
    power = ['rich', 'wings', 'genius']
    def fly(ttt, varx, vary):
        print("batman can fly")
        print(varx)
        print(vary)
    dataa = 3
    gf = 'rachel'


# In[46]:


objb = batman()


# In[47]:


objb.fly(67, 89)


# In[48]:


class batman:
    power = ['rich', 'wings', 'genius']
    def fly(self, varx, vary):
        print("batman can fly")
        print(varx)
        print(vary)
    dataa = 3
    gf = 'rachel'


# In[52]:


class diana:
    power = ['rich', 'lasso', 'shield']
    dataa = 3    
    def fly(self, varx, vary):
        print("diana can jump")
        print(varx)
        print(vary)
        print(self.dataa)
        #obj.dataa


# In[53]:


objc = diana()


# In[54]:


objc.fly(6,7)


# In[55]:


class diana:
    power = ['rich', 'lasso', 'shield']
    dataa = 3    
    def fly(self, varx, vary):
        print("diana can jump")
        print(varx)
        print(vary)
        self.newdata = 22
        print(self.dataa)
        print(self.newdata)
        #obj.dataa


# In[56]:


objd = diana()


# In[57]:


objd.dataa


# In[58]:


objd.newdata


# In[60]:


objd.fly(6,7)


# In[61]:


objd.newdata


# In[62]:


obje = diana()


# In[68]:


class aquaman:
    power = ['rich', 'lasso', 'shield']
    dataa = 3    
    def __init__(self):
        print("gets called automatically")
    def fly(self):
        print("diana can jump")


# In[69]:


objp = aquaman()


# In[78]:


class aquaman:
    power = ['rich', 'lasso', 'shield']
    dataa = 3    
    def __init__(self, d):
        self.dataa = d
        print("gets called automatically")
    def fly(self):
        print("diana can jump")


# In[74]:


objq = aquaman(556)


# In[75]:


objq.dataa


# In[76]:


objr = aquaman()


# In[79]:


class flash:
    vara = 30
    _varb = 40
    __varc = 50
    __vard__ = 60
    def fly(self):
        print(self.vara)
        print(self._varb)
        print(self.__varc)
        print(self.__vard__)
        


# In[80]:


objf = flash()


# In[81]:


objf.fly()


# In[82]:


print(objf.vara)
print(objf._varb)
print(objf.__varc)
print(objf.__vard__)


# In[83]:


print(objf.vara)
print(objf._varb)


# In[84]:


print(objf.__varc)
       # print(objf.__vard__)


# In[85]:


print(objf.__vard__)


# In[89]:


class robot:
    "half human half robot"
    vara = 30
    _varb = 40
    __varc = 50
    __vard__ = 60
    def fly(self):
        print(self.vara)
        print(self._varb)
        print(self.__varc)
        print(self.__vard__)
    def __run(self):
        print("run")


# In[90]:


objo = robot()


# In[88]:


objo.__run()


# In[91]:


print(robot.__doc__)


# In[92]:


help(robot)


# In[ ]:




