print("Please enter numbers in console")

maxnum = None
minnum = None

while True:
    newnum = input("Enter number:")

    if newnum == "done":
        break

    try:
        newnum = int(newnum)
    except:
        print("Please enter only numbers")
        continue

    if maxnum is None:
        maxnum = newnum
        minnum = newnum

    if maxnum < newnum: maxnum = newnum
    if minnum > newnum: minnum = newnum

print("Maxnum is", maxnum)
print("Minnum is", minnum)