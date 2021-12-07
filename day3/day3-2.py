# %%
import collections
inputfile = open('./day3-example.txt')
lines = inputfile.readlines()
co2 = o2 = nums = [i.strip('\n') for i in lines]

for i in range(len(nums[0])):
    newList = []
    tempList_o2 = [ o2[j][i] for j in range(len(o2))]
    tempList_co2 = [ co2[j][i] for j in range(len(co2))]
    if len(o2) > 1:
        most_common_o2 = collections.Counter(tempList_o2).most_common()
        if most_common_o2[0][1] == most_common_o2[1][1]:
            o2Keep = 1
        else: o2Keep = str(most_common_o2[0][0])
    if len(co2) > 1: 
        most_common_co2 = collections.Counter(tempList_co2).most_common()
        if most_common_co2[0][1] == most_common_co2[1][1]:
            co2Keep = 0
        else: co2Keep = str(most_common_co2[1][0])
    if len(co2) > 1:
        for num in co2:
            if num[i] == co2Keep:
                newList.append(num)
        co2 = newList
    newList = []
    if len(o2) > 1:
        for num in o2:
            if num[i] == o2Keep:
                newList.append(num)
        o2 = newList
print (int(o2[0],2)*int(co2[0],2))


    
        
    
    

        
#%%

for i in range(len(gamma)):
    gamma[i] = str(int(gamma[i]))
    epsilon[i] = str(int(epsilon[i]))

print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))
# %%