#!/usr/bin/env python
# coding: utf-8

# In[2]:


from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")


def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)


# In[9]:


from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained("zf_model", num_labels=2)

from transformers import TextClassificationPipeline

pipe = TextClassificationPipeline(model=model, tokenizer=tokenizer, top_k = 1)


# In[24]:


def djdm(text):
    if(pipe(text)[0][0]['label']=='LABEL_1'):
        return True
    else:
        return False


# In[25]:


djdm("im dpressed lol")


# In[ ]:




