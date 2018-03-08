
# coding: utf-8

# In[1]:


import requests


# In[4]:


from bs4 import BeautifulSoup


# In[5]:


import csv


# In[6]:


resp=requests.get('https://djmag.com/top100djs')


# In[8]:


html_str=resp.text


# In[9]:


document=BeautifulSoup(html_str,'html.parser')


# In[13]:


list_name=[]


# In[14]:


list_grade=[]


# In[15]:


names=document.find_all('div',attrs={'class':'top100dj-name'})


# In[16]:


for name in names:
    a=name.find('a')
    list_name.append(a.text)
    print(a.text)


# In[17]:


grades=document.find_all('div',attrs={'class':'top100dj-movement'})


# In[19]:


for grade in grades:
    list_grade.append(grade.text)
    print(grade.text)


# In[20]:


with open('DJmag.csv','w') as f:
    writer=csv.writer(f)
    for i in range(0,len(list_name)):
        writer.writerow([list_name[i],list_grade[i]])

