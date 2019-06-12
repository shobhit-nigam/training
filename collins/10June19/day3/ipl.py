#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


path = "matches.csv"
matches = pd.read_csv(path)


# In[4]:


matches


# In[5]:


matches.shape


# In[6]:


matches.columns


# In[7]:


matches.info()


# In[9]:


matches.head()


# In[10]:


matches.shape[0]


# In[13]:


matches['id'].max()


# In[14]:


matches_2017 = matches[matches['season'] == 2017]


# In[15]:


matches_2017


# In[16]:


matches_2017.shape


# In[17]:


matches['season'].unique()


# In[18]:


len(matches['season'].unique())


# In[19]:


m17 = matches_2017 


# In[20]:


m17.columns


# In[21]:


right = m17[m17['winner']==m17['toss_winner']]


# In[22]:


right.shape

right
# In[23]:


right


# In[25]:


percentage = (right.shape[0]/m17.shape[0])*100


# In[26]:


percentage


# In[28]:


last_match = m17.tail(1)


# In[29]:


last_match


# In[30]:


last_match['winner']


# In[32]:


dl_used = matches[matches['dl_applied'] == 1]


# In[33]:


dl_used


# In[34]:


dl_used.shape[0]


# In[35]:


dl_used['city'].count()


# In[36]:


dl_city = dl_used['city'].value_counts()


# In[37]:


dl_city


# In[38]:


type(dl_city)


# In[39]:


type(dl_used)


# In[40]:


sns.countplot(x='city', data=dl_used)
plt.show()


# In[41]:


sns.countplot(y='city', data=dl_used)
plt.show()


# In[42]:


matches.columns


# In[44]:


matches.iloc[matches['win_by_runs'].idxmax()]


# In[45]:


matches.iloc[matches['win_by_runs'].idxmax()]['winner']


# In[47]:


matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()]['winner']


# In[48]:


sns.countplot(x='season', data=matches)
plt.show()


# In[50]:


sns.countplot(y='winner', data = matches)
plt.show()


# In[51]:


matches.columns


# In[52]:


sns.countplot(y = 'player_of_match', data = matches)
plt.show()


# In[53]:


top_players = matches.player_of_match.value_counts()[:10]


# In[54]:


sns.barplot(y = top_players.index, x = top_players)


# In[59]:


import time
def taska():
    print("in task a ")
    time.sleep(8)
    print("task a will exit")

def taskb():
    print("in task b ")
    time.sleep(4)
    print("task b will exit")


# In[56]:


def maintask():
    print("in main task")
    taska()


# In[60]:


def maintask():
    print("in main task")
    taska()
    taskb()
    print("main will get engaged")
    time.sleep(12)
    print("main got up")


# In[61]:


maintask()


# pass

# In[63]:


import threading
def maintask():
    print("in main task")
    ta = threading.Thread(target = taska)
    tb = threading.Thread(target = taskb)
    ta.start()
    tb.start()
    print("main will get engaged")
    time.sleep(12)
    print("main got up")
    


# In[64]:


maintask()


# In[65]:


maintask()


# In[68]:


import threading
import time
def taska():
    print("in task a ")
    time.sleep(8)
    print("task a will exit")

def taskb():
    print("in task b ")
    time.sleep(12)
    print("task b will exit")

def maintask():
    print("in main task")
    ta = threading.Thread(target = taska)
    tb = threading.Thread(target = taskb)
    ta.start()
    tb.start()
    print("main will get engaged")
    time.sleep(4)
    print("main got up")
    ta.join()
    tb.join()
    print("last line")


# In[67]:


maintask()


# In[69]:


maintask()


# In[ ]:




