#!/usr/bin/env python
# coding: utf-8

# In[68]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import scipy.stats as stats
import re


import datetime


# In[88]:


other_train = pd.read_csv("dataset/other_train.csv")
other_valid = pd.read_csv("dataset/other_valid.csv")
personal_train = pd.read_csv("dataset/personal_train.csv")
personal_valid = pd.read_csv("dataset/personal_valid.csv")


# In[70]:


other_train.head()


# In[71]:


personal_train.head()


# In[72]:


personal_train.describe(include='all')


# In[73]:


personal_train.columns.unique()


# In[74]:


def normalize_date(x):
    x = re.sub(r"([0-9]{4}-[0-9]{2}-[0-9]{2}) 00[: ]?00[: ]?00",r"\1", x.strip())
    x = re.sub(r"([0-9]{2})\/([0-9]{2})\/([0-9]{4})",r"\3-\2-\1", x)
    x = re.sub(r"([0-9]{4})\/([0-9]{2})\/([0-9]{2})",r"\1-\2-\3", x)
    x = re.sub(r"(^[0-9]{2})-([0-9]{2})-([0-9]{2})",r"19\1-\2-\3", x)
    return x

personal_train['date_of_birth'] = personal_train['date_of_birth'].apply(normalize_date)
personal_train['date_of_birth'] = pd.to_datetime(personal_train['date_of_birth'])
personal_train['date_of_birth']

personal_valid['date_of_birth'] = personal_valid['date_of_birth'].apply(normalize_date)
personal_valid['date_of_birth'] = pd.to_datetime(personal_valid['date_of_birth'])
personal_valid['date_of_birth']


# In[75]:


other_train.columns.unique()


# In[97]:


other_train.pregnant.isna().unique()


# In[105]:


def normalize_pregnancy(x):
    if not isinstance(x, str):
        return x
    x = re.sub(r"^f$|(^F$)|(^FALSE$)", r"0", x)
    x = re.sub(r"^t$|^T$|^TRUE$", r"1", x)
    return int(x)

other_train.pregnant = other_train.pregnant.apply(normalize_pregnancy)
other_train.pregnant 


# In[ ]:





# In[ ]:




