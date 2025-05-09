# Question :
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
       # An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
# Example 1:
    # Input: s = "racecar", t = "carrace"
    # Output: true

# Solution 1: using sorting

def is_anagram_sort(s,t):
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)

# The sorted() function is a built-in Python function that returns a new sorted list from the elements of any iterable (like strings, lists, tuples).


# Solution 2 : using 1 hashmap

def is_anagram(s,t):
    if len(s) != len(t):
        return False
     
    count = {}
    if i in range(len(s)):
         count[s[i]] = count.get(s[i], 0) + 1
         count[t[i]] = count.get(t[i], 0) - 1
    for val in count.values():
        if val != 0:
            return False
    return False

# Solution : 3 using 2 hashmaps
def valid_anagram(s, t):
    count_s = {}
    count_t = {}

    for ch in s:
        count_s[ch] = count_s.get(ch, 0) + 1
    for ch in t:
        count_t[ch] = count_t.get(ch, 0) + 1

    return count_s == count_t

