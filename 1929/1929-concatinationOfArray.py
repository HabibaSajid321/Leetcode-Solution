# Solution on 
# simply using + operator for concatination

def concatinationNums(nums):
    return nums + nums
# it will simply add nums with nums

# Solution 2
# using itration with loop

def concatinationLoop(nums):
    ans = []
    for i in nums:
        ans.append(i)
    return ans + ans

# Version	              Time Complexity	   Space Complexity	           Notes
# nums + nums                	O(n)	            O(n)           	Easiest and clean
# Loop + ans + ans	            O(n)	            O(n)	        Works, but creates intermediate list