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
 k, return the number of subarrays where the product of 
 all the elements in the subarray is strictly less than k.
 
 For example, given the input nums = [10, 5, 2, 6], k = 100, 
 the answer is 8. The subarrays with products less than k are:

 [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
  
"""

# Function to find number of subarrays whose product is less than k
# Time Complexity: O(n)
# Space Complexity: O(1)
def num_subarray_product_less_than_k(nums, k):
    if k <= 1:
        return 0

    ans = left = 0
    curr = 1

    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1
        ans += right - left + 1

    return ans

 
nums = [10, 5, 2, 6]
targetProduct = 100
print("nums: " + str(nums)  + " targetProduct: " + str(targetProduct) + " numSubarrayProduct: " + str(num_subarray_product_less_than_k(nums, targetProduct)))

