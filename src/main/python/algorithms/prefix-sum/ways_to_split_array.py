"""
 Author: Francisco Franco

 Prefix sum is a technique that can be used on arrays (of numbers). 
 The idea is to create an array prefix where prefix[i] is the sum 
 of all elements up to the index i (inclusive). For example, given 
 nums = [5, 2, 1, 6, 3, 8], we would have prefix = [5, 7, 8, 14, 17, 25].
 
 Given an integer array nums, find the number of ways to split the array 
 into two parts so that the first section has a sum greater than or equal 
 to the sum of the second section. The second section should have at least 
 one number.

"""

# Function to find subarray max sum for target size k
# Without prefix sum, Time Complexity: O(n*m)
# With prefix sum, Time Complexity: O(n+m)
# Space Complexity: O(n)
def waysToSplitArray(nums) -> int:
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1
            
    return ans

nums = [10, 4, -8, 7]
print("nums: " + str(nums) + " numOfWays: " + str(waysToSplitArray(nums)))

