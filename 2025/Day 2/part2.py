from typing import List, Tuple

def parse_ranges() -> List[Tuple[int, int]]:
    with open('input.txt', "r", encoding="utf-8") as f:
        text = f.read().strip()
    if not text:
        return []

    parts = [p.strip() for p in text.split(",") if p.strip()]
    result: List[Tuple[int, int]] = []
    for token in parts:
        if "-" not in token:
            raise ValueError(f"Unexpected token while parsing ranges: {token!r}")
        a, b = token.split("-", 1)
        result.append((int(a), int(b)))

    return result

def find_invalid_ids(bounds: Tuple[int, int]) -> List[int] :
    invalid_ids = []
    for i in range(bounds[0], bounds[1] + 1):
        if check_repetition(i):
            # print(i)
            invalid_ids.append(i)
    return invalid_ids

def check_repetition(id: int) -> bool:
    id = str(id)
    divisors = find_divisors(len(id))
    for d in divisors:
        parts = len(id) // d
        sequences = split_string_into_n_parts(id, parts)
        if all(seq == sequences[0] for seq in sequences) and len(sequences) > 1:
            return True

    return False


def find_divisors(n: int) -> List[int]:
    if n <= 0:
        return []

    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice
                divisors.append(n // i)

    return sorted(divisors, reverse=True)


def split_string_into_n_parts(s: str, n: int) -> List[str]:
    if n <= 0:
        return []

    part_length = len(s) // n

    if len(s) % n != 0:
        raise ValueError(f"String length {len(s)} is not divisible by {n}")

    return [s[i * part_length: (i + 1) * part_length] for i in range(n)]


if __name__ == "__main__":
    ranges = parse_ranges()
    print(ranges)
    invalid_ids = []
    for bound in ranges:
        invalid_ids += find_invalid_ids(bound)
    print(sum(invalid_ids))

