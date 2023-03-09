from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
# YOUR ANSWER
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return print([i, j])

twoSum([1,2,5],7)