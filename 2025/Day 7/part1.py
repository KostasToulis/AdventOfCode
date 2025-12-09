if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    input_data = [[list(item) for item in line.rstrip('\n').split()] for line in input_data]


    split = 0

    for i in range(1, len(input_data)):
        prev = input_data[i-1][0]
        row = input_data[i][0]
        for j in range(1, len(row)-1):
            if prev[j] == 'S':
                row[j] = '|'
            if prev[j] == '|':
                if row[j] == '^':
                    row[j-1] = '|'
                    row[j+1] = '|'
                    split += 1
                else:
                    row[j] = '|'

    for row in input_data:
        print(''.join(row[0]))
    print(split)