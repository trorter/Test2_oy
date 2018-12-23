import random

total = 0.0
count = 0

for i in range(1000000):
    randprice = random.randint(0, 100)
    randdeel = random.randint(0, 100)
    #print(randprice)
    #print(randdeel)
    #print("=====")
    if randdeel >= randprice:
        sumdeal = (randprice * float(1.5)) - randdeel
        total = total + sumdeal
        count = count + 1

print("total=", total)
print("count=", count)
print("total aver=", total/count)
