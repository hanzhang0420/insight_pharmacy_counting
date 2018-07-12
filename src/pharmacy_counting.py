
# coding: utf-8

# ## Insight pharmacy counting problem

# In[524]:


import sys
# input file
input_file = sys.argv[1]
output_file= sys.argv[2]
#input_file = '../insight_testsuite/tests/test_1/input/itcont.txt'#../input/itcont.txt' 


# In[523]:


with open(input_file,'r') as f:
    header=f.readlines(10)
f.close()   
print('header',header) # header of the input file 


# In[514]:


# readin data line by line
prescriber=[]
drug_name=[]
drug_cost=[]
with open(input_file,'r') as f:
    next(f) # skip the first line 
    for line in f.readlines():
        prescriber.append(line.replace('\n', '').split(',')[1]+line.replace('\n', '').split(',')[2])
        drug_name.append(line.replace('\n', '').split(',')[3])
        drug_cost.append(line.replace('\n', '').split(',')[4])
f.close()


# In[515]:


#print('Number of Drug',len(set(drug_name)))


# In[516]:


# drug_name & drug_cost 
name_cost=tuple(zip(drug_name,drug_cost))


# In[517]:


total_cost={}  # add up the cost of drug using the drug name as key 
for name,cost in name_cost:
    # format float or int 
    if len(cost.split('.'))>1:
        cost=float(cost)
    else:
        cost=int(cost)
        
    if name in total_cost:
        total_cost[name] += (cost)
    else:
        total_cost[name]=(cost)       


# In[518]:


# drug_name & prescriber
name_pres=tuple(zip(drug_name,prescriber))
#name_pres


# In[519]:


# number of prescriber 
num_prescriber={}         # count the number of prescribers based on the drug name as key 
for name,pres in name_pres:
    pres_u=[]  
    if name in num_prescriber:
        num_prescriber[name].append(pres) 
    else:
        pres_u.append(pres)
        num_prescriber[name]=(pres_u)
        

for name in set(drug_name):  #UNIQUE of prescriber 
    #print(name)
    num_prescriber[name]=len(set(num_prescriber[name]))    


# In[520]:


#write output file

with open(output_file,'w') as f:
    f.write('drug_name,num_prescriber,total_cost') #header
    f.write('\n')
    for name in sorted(total_cost, key=total_cost.get, reverse=True):  #in descending order 
        count=str(num_prescriber[name])
        tot=str(total_cost[name])
        f.write('%s' %(','.join((name,count,tot))))
        f.write('\n')
        
    f.truncate(f.tell()-1) # remove the newline at the very end 
f.close()        

