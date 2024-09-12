from tester import test


# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence


"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:
0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""


# move forward recursively
def solution_one(s:str, t:str) -> bool:
    if s == "":
        return True
    if t == "":
        return False
    def f(i, j):
        if i == len(s)-1 and s[i] == t[j]:
            return True
        if j == len(t)-1:
            return False
        if s[i] == t[j]:
            i+=1
        j+=1
        return f(i, j)
    return f(0, 0)


# move backward recursively
def solution_two(s:str, t:str) -> bool:
    if s == "":
        return True
    if t == "":
        return False
    def f(i, j):
        if i == 0 and s[i] == t[j]:
            return True
        if j == 0:
            return False
        if s[i] == t[j]:
            i-=1
        j-=1
        return f(i, j)
    return f(len(s)-1, len(t)-1)


# move forward iteratively
def solution_three(s:str, t:str) -> bool:
    if s == "":
        return True
    i = 0
    for j in range(len(t)):
        if s[i] == t[j]:
            i+=1
            if i == len(s):
                return True
    return False


# TESTING
# --------------------

test_cases = [
    [["abc", "abcde"], True],
    [["aec", "abcde"], False],
    [["", "abcde"], True],
    [["abc", ""], False],
    [["a", "b"], False],
    [["b", "a"], False],
    [["aa", "aa"], True],
    [["ab", "ba"], False],
    [["ba", "ab"], False],
    [["asd", "asfg"*100+"d"], True],
]

test(solution_one, test_cases)
test(solution_two, test_cases)
test(solution_three, test_cases)
