#%%
inputfile = open('./day2-input.txt')
lines = inputfile.readlines()
tuplesList = [ tuple(i.split()) for i in lines ]
x = y = 0
for i,j in tuplesList:
    j = int(j)
    if i.lower() == 'forward':
        x += j
    elif i.lower() == 'down':
        y += j
    elif i.lower() == 'up':
        y -= j
print(x*y)
# %%
