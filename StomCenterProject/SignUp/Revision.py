# l1=[1,2,3,4,5,6,7]
# def division(elem):
#     return elem%2
# # print(list(map(division,l1)))

import random
randomlist = []
for i in range(0,10000):
    n = random.randint(1,100000)
    randomlist.append(n)
def func(elem):
    if elem>99999:
        return True
print(len(list(filter(func,randomlist))))

