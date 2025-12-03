
if __name__ == '__main__':

    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    max_joltages = []
    for bank in input_data:
        bank = bank.strip()
        joltages = [x for x in bank]
        max_joltage = []
        c = 0
        index = -1
        while (len(max_joltage) < 12):
            max_digit = 0

            for i in range(index + 1, len(joltages)-11+c):
                if int(joltages[i]) > max_digit:
                    max_digit = int(joltages[i])
                    index = i
            max_joltage.append(str(max_digit))
            c += 1

        max_joltages.append(int(''.join(max_joltage)))
    print(sum(max_joltages))