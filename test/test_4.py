fname = input("Enter file name: ")

try:
    cfile = open(fname)
except:
    print("File not found")
    quit()

listofwords = list()

for line in cfile:
    for word in line.split():
        if word in listofwords: continue
        listofwords.append(word)

listofwords.sort()

print(listofwords)