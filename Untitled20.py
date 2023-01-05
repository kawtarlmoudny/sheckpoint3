#!/usr/bin/env python
# coding: utf-8

# In[1]:


res=1
sample=[2,3,6]
for i in sample:
    res = res*i
print(res)    


# In[2]:


sample2=[(2,5),(1,2),(4,4),(2,3)]
key= lambda x: x[1]
result=sorted(sample2,key=lambda x:x[1])
result


# In[5]:


d1={'a':100,'b':200,'c':300}
d2={'a':100,'b':200,'d':400}
D=set(d1.keys()).union(set(d2.keys()))
DD={}
for i in D:
    DD[i]=d1.get(i,0)+d2.get(i,0)
print(DD)


# In[10]:


lis=[('item1','12,20'),('item2','15.10'),('item3','24,5')]
sorted(lis,reverse = True)


# In[ ]:




