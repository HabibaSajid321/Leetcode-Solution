# Question : Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# Example 1:
# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Solution 1: Brute force using nested loops

def two_sum(self,nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i , j]
    return []

# Time complexity: O(n²)  
# Space complexity: O(1)

# Solution 2: using hashmap

def twoSum(self, nums, target):
    hashMap = {}

    for i , n in enumerate(nums):
        diff = target - n 
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[n] = i

# Time complexity: O(n)  
# Space complexity: O(n)