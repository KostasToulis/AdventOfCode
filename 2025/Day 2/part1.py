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
    if len(id)%2 == 0:
        half = len(id)//2
        if id[:half] == id[half:]:
            return True
    return False


if __name__ == "__main__":
    ranges = parse_ranges()
    print(ranges)
    invalid_ids = []
    for bound in ranges:
        invalid_ids += find_invalid_ids(bound)
    print(sum(invalid_ids))

