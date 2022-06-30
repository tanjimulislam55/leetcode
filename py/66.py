from typing import List


def plus_one(digits: List[int]) -> List[int]:
    return [int(e) for e in str(int("".join(str(e) for e in digits)) + 1)]


print(plus_one([4, 3, 2, 1]))
