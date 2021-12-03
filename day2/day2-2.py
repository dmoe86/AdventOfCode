#%%
inputfile = open('./day2-input.txt')
lines = inputfile.readlines()
tuplesList = [ tuple(i.split()) for i in lines ]
x = y = aim = 0
for i,j in tuplesList:
    j = int(j)
    if i.lower() == 'down':
        aim += j
    elif i.lower() == 'up':
        aim -= j
    elif i.lower() == 'forward':
        x += j
        y += aim * j
print(x*y)
# %%
