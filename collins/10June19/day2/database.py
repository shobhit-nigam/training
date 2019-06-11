#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[3]:


con = sqlite3.connect('cricket.db')


# In[4]:


cursor_obja = con.cursor()


# In[5]:


cursor_obja.execute("CREATE table players(id integer PRIMARY KEY, name text, team text, skill text, price real, country text)")


# In[6]:


cursor_obja.execute("""INSERT into players VALUES (23, 'yuvi', 'mi', 'b_all', 2567835, 'ind') """)


# In[7]:


con.commit()


# In[8]:


cursor_obja.execute("""INSERT into players(id, name, team, skill, price, country) VALUES (?,?,?,?,?,?)""", [22, "bumrah" , "mi", "bowler", 762945, 'ind'])


# In[9]:


con.commit()


# In[10]:


lista = [34, 'jadeja', 'csk', 'bowl_allrounder', 7834356, 'ind']


# In[11]:


query = """INSERT into players(id, name, team, skill, price, country) VALUES (?,?,?,?,?,?)"""


# In[12]:


cursor_obja.execute(query, lista)


# In[13]:


con.commit()


# In[14]:


cursor_obja.execute("UPDATE players SET name = 'sirjadeja' where id = 34")


# In[15]:


con.commit()


# In[16]:


cursor_obja.execute('SELECT id, name from players')


# In[17]:


rows = cursor_obja.fetchall()


# In[18]:


type(rows)


# In[19]:


print(rows)


# In[21]:


cursor_obja.execute("""select name from sqlite_master where type = 'table' """)


# In[22]:


cursor_obja.fetchall()


# In[24]:


cursor_obja.execute(""" drop table if exists 'sampl'""")


# In[25]:


data = [(31, 'abd'), (32, 'ponting'), (33, 'butler'), (34, 'gayle')]


# In[26]:


cursor_obja.execute("create table if not exists cricketers(id integer, name text)")


# In[27]:


con.commit()


# In[28]:


data


# In[29]:


cursor_obja.executemany("""INSERT into cricketers VALUES (?,?)""", data)


# In[30]:


con.commit()


# In[31]:


con.close()


# In[ ]:




