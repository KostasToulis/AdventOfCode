from itertools import zip_longest, product
import math

def apply_operation(oper, numbers):
    if oper == '+':
        return sum(numbers)
    else:
        return math.prod(numbers)


if __name__ == '__main__':
    with open('sample.txt', 'r') as file:
        input_data = file.readlines()
    cols = [col for col in zip_longest(*input_data, fillvalue='')]
    print(cols)


    numbers = []
    result = 0
    oper = ''
    for i, col in enumerate(cols):
        if col[-1].strip() != '':
            numbers = []
            oper = col[-1].strip()
        numbers.append(col[:-1])
        if i < len(cols)-1 and cols[i+1][-1].strip() != '':
            # print(numbers)
            data = [int(''.join(row)) for row in zip(*numbers)]

            print(f'Applying operation {oper} to {data}')
            result += apply_operation(oper, data)
        if i == len(cols)-1:
            data = [int(''.join(row)) for row in zip(*numbers)]
            print(f'Applying operation {oper} to {data}')
            result += apply_operation(oper, data)
    print(result)