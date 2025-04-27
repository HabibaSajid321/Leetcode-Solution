# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct. 
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Approach 1: Using nested loop 

def is_duplicate_loop(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False


# Approach 2: check duplicate by sorting the array 

def is_duplicate_sort(arr):
    arr.sort()
    for i in range(len(arr)- 1):
        if arr[i] == arr[i + 1]:
            return True
    return False

# Approach 3: # check duplicate by using set

def is_duplicate_set(arr):
    return len(arr) != len(set(arr))


# Approach 4 : # check duplicate by using hashmap

def is_duplicate_hashmap(arr):
    hashmap = {}
    for i in arr:
        if i in hashmap:
            return True
        hashmap[i] = 1
    return False

# Space and time complexity
# Approach	                Time Complexity	                 Space Complexity
# Nested Loop	                O(n²)	                         O(1)
# Sorting + Compare	            O(n log n)	                     O(1) or O(n)
# Using Set	                    O(n)	                         O(n)
# Using Hashmap	                O(n)	                         O(n)