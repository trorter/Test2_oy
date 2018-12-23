#fname = input("Enter file name: ")
fname = '/Users/andrey/ttt.txt'

try:
    cfile = open(fname)
except:
    print("File not found")
    quit()

counts = dict()

for line in cfile:
    if not line.startswith("From"): continue
    if len(line.split()) < 3: continue

    hour = line[(line.find(':')-2):line.find(':')]

    counts[hour] = counts.get(hour, 0) + 1

sortedMap = sorted([(k, v) for k, v in counts.items()])

for k,v in sortedMap: print(k, v)