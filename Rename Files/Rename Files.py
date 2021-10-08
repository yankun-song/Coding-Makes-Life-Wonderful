#!/usr/bin/env python
# coding: utf-8

# In[23]:


import os
import re

def changeFileName(path):
    # change current directory to the given path
    os.chdir(path)
    # get all the filenames
    dirs = os.listdir(path)
    
    for old_name in dirs:
        name_components = old_name.split(".")
        to_modify = name_components[0]
        # extract the No. of problems
        old_num = re.findall("\d+", to_modify)[0]
        zeros = 4 - len(old_num)
        new_num = "0" * zeros + old_num
        new_name = old_name.replace(old_num, new_num)
         
        #replace
        os.rename(old_name, new_name)
        
        


# In[24]:


path = r"/Users/yankunsong/Desktop/leetcode/Solutions"

changeFileName(path)


# In[ ]:




