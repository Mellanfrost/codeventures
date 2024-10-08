from tester import test


# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number


"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:
0 <= n <= 30
"""


# Problem Visualization
#   n   0   1   2   3   4   5   6   7
#   F   0   1   1   2   3   5   8   13


# recursion
def solution_one(n:int) -> int:
    if n <= 1:
        return n
    return solution_one(n-1) + solution_one(n-2)


# recursion with memoization
def solution_two(n:int) -> int:
    seen = {}
    def f(n):
        if n <= 1:
            return n
        if n in seen:
            return seen[n]
        seen[n] = f(n-1) + f(n-2)
        return seen[n]
    return f(n)


# iterative
def solution_three(n:int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


# TESTING
# --------------------

test_cases = [
    [[0], 0],
    [[1], 1],
    [[2], 1],
    [[3], 2],
    [[4], 3],
    [[5], 5],
    [[6], 8],
    [[7], 13],
    [[20], 6765],
    [[30], 832040],
]

test(solution_one, test_cases[:-2:]) # excluding last 2 tests as this solution is slow
test(solution_two, test_cases)
test(solution_three, test_cases)
