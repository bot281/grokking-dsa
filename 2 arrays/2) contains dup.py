# given int array nums, return true if any val shows up at least 2x, but false if every element is unique

sample = [1,2,3]

temp = []

for n in sample:
    if n in temp:
        print(True)
        break
    else:
        temp.append(n)
else:
    print(False)