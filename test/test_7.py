fname = input("Enter file name: ")

try:
    cfile = open(fname)
except:
    print("File not found")
    quit()

counts = dict()

for line in cfile:
    if not line.startswith("From"): continue
    if len(line.split()) < 3: continue

    counts[line.split()[1]] = counts.get(line.split()[1], 0) + 1

#print(counts)

bigCount = 0
bigMail = None

for k, v in counts.items():
    #print(k, v, bigCount, bigMail)
    if (bigCount is None) or (v > bigCount):
        bigCount = v
        bigMail = k

print(bigMail, bigCount)