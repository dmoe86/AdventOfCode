#%%
inputfile = open('./day2-input.txt')
lines = inputfile.readlines()
tuplesList = [ tuple(i.split()) for i in lines ]
x = y = 0
for i,j in tuplesList:
    if i.lower() == 'forward':
        x += int(j)
    elif i.lower() == 'down':
        y += int(j)
    elif i.lower() == 'up':
        y -= int(j)
print(x*y)



# %%
