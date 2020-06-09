import random
# print(dir(range))
pick = random.choice(range(10))
print(pick)

pick = random.choice([1,2,3,4,5])
print(pick)

# help(random.choice) q누르면 나오기

# help(random.sample)

pick = random.sample(range(10),3)

