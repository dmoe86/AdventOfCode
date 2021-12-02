inputFile = open("./1-1_inputs.txt")
lines = inputFile.readlines()
nums = [ int(i) for i in lines ]
counter = 0
for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        counter += 1
print(counter)