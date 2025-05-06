# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Solution 1: using sorting 

def group_anagram(self, strs):
    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())
# defaultdict is a class from Python's collections module.
# It works like a regular dictionary, but it provides a default value for keys that don't exist instead of throwing a KeyError.


# Solution : 2 using hashmap

def group_Anagram(self, strs):
    d = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26

        for letter in s:
            count[ord(letter) - ord('a')] += 1

        d[tuple(count)].append(s)
    return d.values()