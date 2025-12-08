from itertools import zip_longest, product
import math
import numpy as np

def apply_operation(oper, numbers):
    if oper == '+':
        return sum(numbers)
    else:
        return math.prod(numbers)


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.readlines()
    cols = [col for col in zip_longest(*input_data, fillvalue='')]


    cols = list(map(lambda x: [c.rstrip('\n') for c in x], cols))
    cols = np.array(cols)
    cols = cols.T

    numbers = []
    result = 0
    oper = ''

    y = len(cols)
    x = len(cols[0])

    for i in range(x):
        if cols[-1, i].strip() != '':
            numbers = []
            oper = cols[-1, i].strip()
        numbers.append(cols[:-1, i])
        if i < x-1 and cols[-1, i+1].strip() != '':
            numbers = [row for row in numbers if any(cell.strip() != '' for cell in row)]

            data = [int(''.join(row)) for row in numbers]

            print(f'Applying operation {oper} to {data}')
            result += apply_operation(oper, data)
        if i == x-1:
            numbers = [row for row in numbers if any(cell.strip() != '' for cell in row)]

            data = [int(''.join(row)) for row in numbers]
            print(f'Applying operation {oper} to {data}')
            result += apply_operation(oper, data)
    print(result)