#%%
import numpy
inputfile = open('./day5-input.txt')
lines = inputfile.readlines()
segments = [line.replace(' -> ',',').strip('\n') for line in lines]
max_x = max(list(numpy.concatenate([[int(x) for x in line.split(',')[::2]] for line in segments])))
max_y = max(list(numpy.concatenate([[int(y) for y in line.split(',')[1::2]] for line in segments])))
vent_map = numpy.zeros((1,max_x+2,max_y+2), dtype=int)

#%%
for line in segments:
    x1,y1,x2,y2 = map(int,line.split(','))
    (x1,y1),(x2,y2) = sorted([(x1,y1),(x2,y2)])
    if y1 == y2:
        for x in range(x1,x2+1):
            vent_map[0,y1,x] += 1
    if x1 == x2:
        for y in range (y1,y2+1):
            vent_map[0,y,x1] += 1
    #diagonals for part 2
    if y1 < y2 and x1 != x2:
        for idx,x in enumerate(range(x1,x2+1)):
            vent_map[0,y1+idx,x] += 1
    if y1 > y2 and x1 != x2:
        for idx,x in enumerate(range(x1,x2+1)):
            vent_map[0,y1-idx,x] += 1

flat_list = list(numpy.concatenate(vent_map).flat)
score = len([i for i in flat_list if i>=2])    
print(score)
# %%
