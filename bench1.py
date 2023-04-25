#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[2]:


nlp = spacy.load("en_core_web_sm")


# In[ ]:


doc = nlp("Apple is looking at buying U.K. startup for $1 billion")


# In[ ]:


for token in doc:
    print(token.text, token.pos_, token.dep_)


# %%

from spacy.lang.yo import Yoruba
nlp = Yoruba()  # use directly
nlp = spacy.blank("yo")  # blank instance
# %%
nlp
# %%
Yoruba()
# %%
import en_core_web_sm
# %%
nlp = en_core_web_sm.load()
doc = nlp("This is a sentence.")
# %%
doc
# %%
nlp("Apple Inc. is an American multinational technology company headquartered in Cupertino, California.")
# %%
