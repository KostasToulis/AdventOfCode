
if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    map = []
    map.append(['.'] * (len(input_data[0].strip()) + 2))
    for line in input_data:
        row = ['.']
        row += [x for x in line.strip()]
        row += ['.']
        map.append(row)
    map.append(['.'] * (len(input_data[0].strip()) + 2))

    for row in map:
        print(''.join(row))

    rolls = 0
    change = True
    while change:
        change = False
        for i in range(1, len(map)-1):
            for j in range(1, len(map[0])-1):
                if map[i][j] == '.' or map[i][j] == 'X':
                    continue
                count = 0
                if map[i-1][j] == '@':
                    count += 1
                if map[i+1][j] == '@':
                    count += 1
                if map[i][j-1] == '@':
                    count += 1
                if map[i][j+1] == '@':
                    count += 1
                if map[i+1][j-1] == '@':
                    count += 1
                if map[i+1][j+1] == '@':
                    count += 1
                if map[i-1][j-1] == '@':
                    count += 1
                if map[i-1][j+1] == '@':
                    count += 1
                if count < 4:
                    rolls += 1
                    map[i][j] = 'X'
                    change = True

    print()
    for row in map:
        print(''.join(row))
    print(rolls)