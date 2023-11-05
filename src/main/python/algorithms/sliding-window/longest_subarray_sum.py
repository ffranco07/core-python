"""
 Author: Francisco Franco

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

 Given an array of positive integers nums and an integer
 k, find the length of the longest subarray whose sum is 
 less than or equal to k. 

"""

# Function to find longest subarray size less than or equal to target sum
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_longest_subarray(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    print("left: " + str(left))
    print("right: " + str(right))

    return ans

nums = [0, -2, 0, -2, -1, 7]
targetSum = 8
print("nums: " + str(nums)  + " targetSum: " + str(targetSum) + " longestSubarray: " + str(find_longest_subarray(nums, targetSum)))

