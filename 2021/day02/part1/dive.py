def main():
    h = 0
    d = 0
    with open("in/2.in") as f:
        for line in f.readlines():
            c, v = line.split()
            v = int(v)
            if c.startswith("f"):
                h += v
            elif c.startswith("d"):
                d += v
            elif c.startswith("u"):
                d -= v

    print(h * d)


if __name__ == "__main__":
    main()
