
def apply_move(curr, operation, zero_counter) -> (int, int) :
    direction = operation[0]
    digits = int(operation[1:])%100
    zero_counter += int(operation[1:])//100
    if direction == 'R':
        if curr + digits > 100:
            zero_counter += 1
        curr = (curr + digits) % 100
    else:
        if (curr - digits) < 0:
            if (curr != 0): zero_counter += 1
            curr = 100 + (curr - digits)

        else:
            curr = curr - digits
    if curr == 0:
        zero_counter += 1
    return (curr, zero_counter)



with open('input.txt', 'r') as file:
    input_data = file.readlines()

zero_counter = 0
curr = 50
for line in input_data:
    (curr, zero_counter) = apply_move(curr, line, zero_counter)
print(zero_counter)




