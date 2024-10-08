
# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes


"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""


def solution_one(nums: list[int]) -> None:
    i=0
    for _ in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
        else:
            i+=1


def solution_two(nums: list[int]) -> None:
    for i in range(len(nums)):
        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)


def solution_three(nums: list[int]) -> None:
    zeroes = nums.count(0)
    for _ in range(zeroes):
        nums.remove(0)
        nums.append(0)
