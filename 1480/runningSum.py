# Solution 1 
# updating the present list 

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

# this Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


# Solution 2 
# using another new list to store 

def newSum(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

# Solution	                     Time Complexity	           Space Complexity
# In-place (modifies input)         	O(n)	                    O(1)
# New list (non-destructive)	        O(n)	                      O(n)