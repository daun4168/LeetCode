# Given an array of integers nums and an integer target, return indices of the t
# wo numbers such that they add up to target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  Only one valid answer exists. 
#  
#  Related Topics Array Hash Table 
#  👍 19629 👎 690


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List, Dict

# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, num1 in enumerate(nums):
            for temp_idx2, num2 in enumerate(nums[idx1 + 1:]):
                idx2 = temp_idx2 + idx1 + 1
                if num1 + num2 == target:
                    return [idx1, idx2]

# One-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict: Dict[int, int] = dict()
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in numdict:
                return [numdict[complement], idx]

            numdict[num] = idx


        
# leetcode submit region end(Prohibit modification and deletion)
