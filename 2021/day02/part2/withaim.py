with open("../in/2.in") as f:
    d = 0
    h = 0
    a = 0
    for line in f.readlines():
        c, v = line.split()
        v = int(v)
        if c.startswith("d"):
            a += v
        elif c.startswith("u"):
            a -= v
        elif c.startswith("f"):
            h += v
            d += a * v
    print(h * d)
