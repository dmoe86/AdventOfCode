# %%
inputfile = open('./day3-input.txt')
lines = inputfile.readlines()
nums = [i.strip('\n') for i in lines]
gamma = []
epsilon = []
for i in range(len(nums[0])):
    total = 0
    for j in nums:
        total += int(j[i])
    gamma.append(total > len(nums)/2)
    epsilon.append(total < len(nums)/2)
for i in range(len(gamma)):
    gamma[i] = str(int(gamma[i]))
    epsilon[i] = str(int(epsilon[i]))

print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))
# %%
