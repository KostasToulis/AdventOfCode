def apply_move(curr, operation) -> int :
    direction = operation[0]
    digits = int(operation[1:])%100
    if direction == 'R':
        curr = (curr + digits) % 100
    else:
        if (curr - digits) < 0:
            curr = 100 + (curr - digits)
            # curr = digits - curr
        else:
            curr = (curr - digits) % 100
    return curr



with open('input.txt', 'r') as file:
    input_data = file.readlines()

zero_counter = 0
curr = 50
for line in input_data:
    curr = apply_move(curr, line)
    if curr == 0:
        zero_counter += 1
print(zero_counter)