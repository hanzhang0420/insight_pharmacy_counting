
# coding: utf-8

# ## Insight pharmacy counting problem

#python 3

import sys
import re
# input file
input_file = sys.argv[1]
output_file= sys.argv[2]


#with open(input_file,'r') as f:
#    header=f.readlines(10)
#f.close()   
#print('header',header) # header of the input file 


# readin data line by line
prescriberid=[] # if the same prescriber same id
drug_name=[]
drug_cost=[]
abnormal=[]
#pattern = '[a-zA-Z0-9,\n]' # only have letters nums , /
#pattern='^[0-9].[0-9]$'
with open(input_file,'r') as f:
    next(f) # skip the first line
    for line in f.readlines():
        if line.strip():
            sep=line.replace('\n', '').split(',')
            #print(sep)
            if bool(re.match('^\d',sep[0])) and bool(re.match('^\d.',sep[-1])):
                prescriberid.append(sep[0])
                drug_cost.append(sep[-1])
                if (line.find('\"')) >=0:
                    try:
                        quote=line.split('\"')[1]
                        new_line=line.replace('\"'+quote+'\"',quote.replace(',',''))
                        drug_name.append(new_line.replace('\n', '').split(',')[-2])
                    except (IndexError, ValueError):
                        print('Unexpected Data')
                        abnormal.append(line)
                        pass
                else:
                    drug_name.append(sep[-2])
            else:
                abnormal.append(line)
f.close()


print('The Number of Lines has unexpected characters',len(abnormal))

print('Number of Unique Drug',len(set(drug_name)))

#==========================================================================================

# drug_name & drug_cost

def sum_keep_precision(f1,f2):     # avoid the floating summaiton problem
    if len(str(f1).split('.'))>1 or len(str(f2).split('.'))>1:
        res=float("%.2f" %(f1+f2))
    else:
        res=int("%d" %(f1+f2))
    return res

drug=(zip(drug_name,drug_cost,prescriberid))

total_cost={}  # add up the cost of drug using the drug name as key
num_prescriber={}

for name,cost,pres in drug:
    # format float or int 

    if len(cost.split('.'))>1:
        cost=float(cost)   # avoid (int('10.000') errors)
    else:
        try:
            cost=int(cost)
        except (ValueError):
            print('Error occurs when converting cost data', cost)
            continue

    if name in total_cost:
        total_cost[name] = sum_keep_precision(total_cost[name],cost)
    else:
        total_cost[name] = cost
    #============================================
    pres_u=[]
    if name in num_prescriber:
        num_prescriber[name].append(pres)
    else:
        pres_u.append(pres)
        num_prescriber[name]=(pres_u)


for name in set(drug_name):  #UNIQUE of prescriber
    #print(name)
    num_prescriber[name]=len(set(num_prescriber[name]))

print('Finish, now writing the output file')
#==============================================================================================

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

print('Done')

