fname = input("Enter file name: ")

try:
    cfile = open(fname)
except:
    print("File not found")
    quit()

listofwords = list()

for line in cfile:
    if not line.startswith("From"): continue
    if '2008' not in line: continue

    listofwords.append(line.split()[1])

for line in listofwords: print(line)

print("\nThere were", len(listofwords), "lines in the file with From as the first word")
