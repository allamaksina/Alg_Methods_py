n = int(input())

lines = []
for _ in range(n):
    temp = list(map(int, input().split()))
    lines.append(temp)


def eval_opt_dots(lines):

    lines.sort(key=lambda z: z[1])

    i = 0
    opt_dots = [lines[i][1]]

    while i < len(lines) - 1:
        i += 1
        if lines[i][0] > opt_dots[-1]:
            opt_dots.append(lines[i][1])

    print(len(opt_dots))
    print(" ".join(map(str, opt_dots)))


eval_opt_dots(n, lines)
