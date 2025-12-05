
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

    count = 0
    for id in ids:
        for r in ranges:
            if id >= r[0] and id <= r[1]:
                count += 1
                break

    print(count)