t = []
ct = 0
with open("../part1/in/1.in", "r") as f:
    for i, line in enumerate(f.readlines()):
        n = int(line)
        if i < 3:
            t.append(n)
        elif sum(t) < sum(t[1:]) + n:
            ct += 1
        t = t[1:] + [n]
print(ct)
