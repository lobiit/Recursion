def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        print("recursion")
        openRussianDoll(doll-1)


openRussianDoll(10)
