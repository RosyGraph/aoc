lvl = 0
ct = 0

with open("in/1.in", "r") as f:
    for i, line in enumerate(f.readlines()):
        n = int(line)
        if i == 0:
            lvl = n
        elif n > lvl:
            ct += 1
        lvl = n

print(ct)
