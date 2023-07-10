#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


data = []
with open("C:/Users/Abdulaziz/Downloads/news.json") as f:
    for i in f:
            data.append(json.loads(i))
            


# In[3]:


courps =[]
courps = [d["short_description"] for d in data] #short description of the dataSet in courps



# In[4]:


#remove punctuation marks from courps
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
x = 0
for i in range(len(courps)):
    for y in courps[i]:
        if y in punc:
            courps[i] = courps[i].replace(y," ")
    #converting words into small letters
    courps[i] = courps[i].lower()  
    


# In[5]:


result = []
#tokenization process
for i in range(len(courps)):
    tokenized = []
    tokenized = courps[i].split()
    result.append(tokenized)


# In[6]:


from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
#store set of stop words in STW
STW = set(stopwords.words('english'))



# In[7]:


WSW = []
sno = nltk.stem.SnowballStemmer('english')
for lst in result:
  #remove stop words and make steamming process after checking that it's not a stopWord 
    filtered_tokens = []
   
    for token in lst:
  
        if token not in STW and len(token)>2:
            filtered_tokens.append(sno.stem(token))

    WSW.append(filtered_tokens)
    
   


# In[8]:


dic = {}
#PART (A) implementation of Inverted Index
for i in range(len(WSW)):
    for token in WSW[i]:
        
            if token not in dic:
                dic[token] = []
            if token in dic:
                dic[token].append(i+1)
    



# In[9]:


import nltk
from nltk.stem import SnowballStemmer
#PART (B) implementation of boolean search

def boolean_search(query, index):
    
    query = query.lower() #convert query into small letter
    
    stem = SnowballStemmer('english')
    
    terms = [stem.stem(term) for term in query.split() if term not in STW] #tokenization,stemming process and remove Stop words for the query

    matchings = set() #set to store the IDs of documents that match the query

    i = 0
    while i < len(terms): # while Loop over the stemmed words in the query
        term = terms[i]

        if '&' not in term: # If the term is a single word, search for its stemmed version in the index
            if term in index:
                matchings.update(index[term])
        else:  # If the term contains the "&" operator, perform an AND search
            and_terms = term.split('&')
            and_matches = set(index.get(and_terms[0], []))
            for and_term in and_terms[1:]:
                and_matches.intersection_update(index.get(and_term, []))
            matchings.update(and_matches)

        i += 1

    return list(matchings)


# In[16]:


import time
que = "BOLLING"
start = time.time()
result = boolean_search(que,dic)
end = time.time()
print(result)
print((end - start)*10**6)


# In[ ]:





# In[ ]:





# In[ ]:




