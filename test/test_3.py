def getnumformstring(curstr):
    return float(curstr[curstr.find('0'):])

#===========

fname = input("Enter filename: ")

try:
    fhandle = open(fname)
except:
    print("File not found")
    quit()

count = 0
summ = 0

for curline in fhandle:
    if not curline.startswith("X-DSPAM-Confidence:"):
        continue

    count = count + 1
    summ = summ + getnumformstring(curline)

#print("count=", count, 'summ=', summ)
print("Average spam confidence: ", float(summ/count))
