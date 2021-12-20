def parse_line(line):
    return [tuple(map(int, s.split(","))) for s in line.rstrip().split(" -> ")]


def read_input(path):
    with open(path, "r") as f:
        return [parse_line(line) for line in f.readlines()]


def hv_lines(coords):
    return (
        [coord for coord in coords if is_hv_line(coord)],
        [coord for coord in coords if not is_hv_line(coord)],
    )


def is_hv_line(coord):
    start, stop = coord
    x1, y1 = start
    x2, y2 = stop
    return (x1 == x2) or (y1 == y2)


def calc_dimensions(coords):
    n = max([max(coord[0][0], coord[1][0]) for coord in coords])
    m = max([max(coord[0][1], coord[1][1]) for coord in coords])
    return n, m


def init_matrix(coords):
    n, m = calc_dimensions(coords)
    return [[0 for _ in range(n + 1)] for _ in range(m + 1)]


def get_start_end(coord):
    x1 = min(coord[0][0], coord[1][0])
    y1 = min(coord[0][1], coord[1][1])
    x2 = max(coord[0][0], coord[1][0])
    y2 = max(coord[0][1], coord[1][1])
    return x1, y1, x2, y2


if __name__ == "__main__":
    hv_coords, diag_coords = hv_lines(read_input("in/2.in"))
    a = init_matrix(hv_coords + diag_coords)
    for coord in hv_coords:
        x1, y1, x2, y2 = get_start_end(coord)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                a[j][i] += 1
    for coord in diag_coords:
        x1, y1 = min(coord)
        x2, y2 = max(coord)
        d = -1 if y2 < y1 else 1
        for i in range(x1, x2 + 1):
            a[y1][i] += 1
            y1 += d
    print(sum(sum(x > 1 for x in row) for row in a))
