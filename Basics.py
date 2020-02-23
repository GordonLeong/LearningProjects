#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_cell_magic('capture', '', '%load_ext sql\n%sql sqlite:///factbook.db')


# In[3]:


get_ipython().run_cell_magic('sql', '', "SELECT * FROM sqlite_master WHERE type = 'table';")


# In[4]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM facts LIMIT 5')


# In[5]:


get_ipython().run_cell_magic('sql', '', 'SELECT MIN(population) min_pop, MAX(population) max_pop, \nMIN(population_growth) min_popgrowth, MAX(population_growth) max_popgrowth\nFROM facts')


# In[7]:


get_ipython().run_cell_magic('sql', '', 'SELECT name \nFROM facts \nWHERE population = (SELECT MIN(population) FROM facts)')


# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT name \nFROM facts \nWHERE population = (SELECT MAX(population) FROM facts)')


# In[13]:


get_ipython().run_cell_magic('sql', '', 'SELECT AVG(population), AVG(area) FROM facts')


# In[14]:


get_ipython().run_cell_magic('sql', '', 'SELECT name \nFROM facts\nWHERE population > (SELECT AVG(population) FROM facts) \nAND area < (SELECT AVG(area) FROM facts)')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




