from typing import List


def search_insert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    count = 0
    while low <= high:
        middle = low + (high - low) // 2
        if target == nums[middle]:
            return middle
        elif target > nums[middle]:
            low = middle + 1
            count = low
        elif target < nums[middle]:
            high = middle - 1
            if nums[high] < target:
                count = high + 1
            else:
                count = high
    return count if count > 0 else 0


print(search_insert([1, 3, 5, 6], 5))
print(search_insert([1, 3, 5, 6], 7))
print(search_insert([1, 3, 5, 6], 2))
print(search_insert([1, 3, 5, 6], 0))
print(search_insert([1, 3], 2))
