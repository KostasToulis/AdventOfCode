
if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        input_data = file.readlines()

    max_joltages = []
    for bank in input_data:
        bank = bank.strip()
        joltages = [int(x) for x in bank]
        max_joltage = 0

        for i in range(len(joltages) - 1):
            for j in range (i+1, len(joltages)):
                joltage = joltages[i] * 10 + joltages[j]
                if joltage > max_joltage:
                    max_joltage = joltage

        max_joltages.append(max_joltage)
    print(sum(max_joltages))