from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
# YOUR ANSWER
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                if i > j :
                    tmp = i
                    i = j
                    j = tmp
                return print([i, j])

# twoSum([1,32,3,9,66,5],33)