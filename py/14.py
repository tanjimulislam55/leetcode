from typing import List


def longest_commont_preffx(arr: List[str]) -> str:
    stack = []
    for x in zip(*arr):
        if len(set(x)) == 1:
            stack.append(x[0])
        else:
            break
    return "".join(stack) if len(stack) > 0 else ""


print(longest_commont_preffx(["flower", "flow", "flight"]))
print(longest_commont_preffx(["dog", "racecar", "car"]))
