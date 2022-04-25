from typing import Optional, List, Dict

"""approach 1"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary: Optional[Dict[int, int]] = {}
        for index in range(len(nums)):
            item = nums[index]
            key = target - item
            if key in dictionary:
                return [dictionary[key], index]
            dictionary[nums[index]] = index

"""approach 2"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary: Optional[Dict[int, int]] = {}
        for count, value in enumerate(nums):
            key = target - value
            if key in dictionary:
                return [dictionary[key], count]
            dictionary.update({value: count})

solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))