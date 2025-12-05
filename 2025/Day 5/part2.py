
if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    ranges = []
    ids = []
    flag = False
    for row in input_data:
        if row.strip() == '':
            flag = True
            continue
        if not flag:
            parts = row.strip().split('-')
            parts = [int(parts[0]), int(parts[1])]
            ranges.append(parts)
        else:
            ids.append(int(row.strip()))

    ranges.sort(key = lambda p: p[0])

    merged = [ranges[0]]

    for r in ranges[1:]:
        last = merged[-1]
        if r[0] <= last[1] + 1:
            last[1] = max(last[1], r[1])
        else:
            merged.append(r)

    count = 0
    for r in merged:
        count += r[1] - r[0] + 1
    print(count)