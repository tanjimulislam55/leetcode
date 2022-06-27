from typing import List


def remove_duplicates(nums: List[int]) -> int:
    new_nums = list(set(nums))
    new_nums.sort()
    for i in range(len(new_nums)):
        nums[i] = new_nums[i]
    return len(new_nums)


print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(remove_duplicates([1, 1, 2]))
