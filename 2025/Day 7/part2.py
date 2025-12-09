if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    # input_data = [[list(item) for item in line.rstrip('\n').split()] for line in input_data]

    input_data = [[list(item.replace('.', '0')) for item in line.rstrip('\n').split()] for line in input_data]

    timelines = 0


    for i in range(1, len(input_data)-1):
        prev = input_data[i-1][0]
        row = input_data[i][0]
        for j in range(1, len(row) -1):

            if prev[j] == 'S':
                row[j] = '1'
                continue
            if row[j] != '^':
                if row[j-1] != '^' and row[j+1] != '^' and prev[j] != '^':
                    row[j] = prev[j]
                elif row[j-1] == '^' and row[j+1] != '^':
                    row[j] = str(int(prev[j]) + int(prev[j-1]))
                elif row[j-1] != '^' and row[j+1] == '^':
                    row[j] = str(int(prev[j]) + int(prev[j+1]))
                elif row[j-1] == '^' and row[j+1] == '^':
                    row[j] = str(int(prev[j]) + int(prev[j-1]) + int(prev[j+1]))





    last_row = input_data[-1][0]
    prev_row = input_data[-2][0]

    for i in range(len(last_row)):
        if prev_row[i] != '.' and prev_row[i] != '^':
            last_row[i] = prev_row[i]

    timelines = sum([int(x) for x in last_row if x != '.' and x != '^'])

    # now replace all 0s with .
    for i in range(len(input_data)):
        row = input_data[i][0]
        for j in range(len(row)):
            if row[j] == '0':
                row[j] = '.'

    for row in input_data:
        print(''.join(row[0]))
    print(timelines+2)