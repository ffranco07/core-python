"""
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

 A sliding window algorithm
 
 A subarray can be defined by two indices, 
 the start and end. For example, with [1, 2, 3, 4], 
 the subarray [2, 3] has a starting index of 1 and 
 an ending index of 2. Let's call the starting index 
 the left bound and the ending index the right bound. 
 Another name for subarray in this context is "window"
 
 In terms of time complexity, any algorithm that looks 
 at every subarray will be at least O(n^2) which is 
 usually too slow. A sliding window guarantees a maximum 
 of 2n window iterations - the right pointer can move 
 n times and the left pointer can move n times. This 
 means if the logic done for each window is O(1), sliding
 window algorithms run in O(n), which is much faster.

"""

# Function to find subarray max sum for target size k
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_max_sum_subarray(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    
    return ans

nums = [6, 1, 6, 8, -3, 100]
targetSize = 2
print("nums: " + str(nums)  + " targetSize: " + str(targetSize) + " maxSum: " + str(find_max_sum_subarray(nums, targetSize)))

