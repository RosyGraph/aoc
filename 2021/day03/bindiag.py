with open("in/2.in", "r") as f:
    a = [line.strip() for line in f.readlines()]
    tmp = a[:]
    for i, _ in enumerate(a[0]):
        h = len(tmp) // 2 + len(tmp) % 2
        if sum([s[i] == "1" for s in tmp]) >= h:
            tmp = [x for x in tmp if x[i] == "1"]
        else:
            tmp = [x for x in tmp if x[i] == "0"]
        if len(tmp) == 1:
            break
    soln = int(tmp[0], 2)
    tmp = a[:]
    for i, _ in enumerate(a[0]):
        h = len(tmp) // 2 + len(tmp) % 2
        if sum([s[i] == "1" for s in tmp]) >= h:
            tmp = [x for x in tmp if x[i] == "0"]
        else:
            tmp = [x for x in tmp if x[i] == "1"]
        if len(tmp) == 1:
            break
    soln *= int(tmp[0], 2)
    print(soln)
