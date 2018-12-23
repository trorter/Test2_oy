import re
from typing import List

#fname = input("Enter file name: ")
#fname = '/Users/andrey/test_sum'
fname = '/Users/andrey/act_data'

try:
    cfile = open(fname)
except:
    print("File not found")
    quit()

numbersList: List[int] = list()

for line in cfile:
    tmpList: List[int] = re.findall('[0-9]+', line)
    if len(tmpList) != 0:
        numbersList = numbersList + tmpList

print(sum(list(map(int, numbersList))))

