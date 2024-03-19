def solution(sizes):
    w = []
    h = []

    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))