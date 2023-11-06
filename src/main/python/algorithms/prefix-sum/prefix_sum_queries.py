"""
 Author: Francisco Franco

 Prefix sum is a technique that can be used on arrays (of numbers). 
 The idea is to create an array prefix where prefix[i] is the sum 
 of all elements up to the index i (inclusive). For example, given 
 nums = [5, 2, 1, 6, 3, 8], we would have prefix = [5, 7, 8, 14, 17, 25].
 
 Given an integer array nums, an array queries where queries[i] = [x, y] 
 and an integer limit, return a boolean array that represents the answer 
 to each query. A query is true if the sum of the subarray from x to y is 
 less than limit, or false otherwise.
 
 For example, given nums = [1, 6, 3, 2, 7, 2], 
 queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is 
 [true, false, true]. For each query, the subarray sums are [12, 14, 12].

"""

# Function to return boolean array if prefix sum indices exceed limit
# Without prefix sum, Time Complexity: O(n*m)
# With prefix sum, Time Complexity: O(n+m)
# Space Complexity: O(n)
def answer_queries(nums, queries, limit):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    ans = []
    for x, y in queries:
        curr = prefix[y] - prefix[x] + nums[x]
        ans.append(curr < limit)

    return ans

nums = [6, 1, 6, 8, -3, 100]
queries = [[0, 3], [2, 5], [2, 4]]
limit = 13
print("nums: " + str(nums)  + " queries: " + str(queries) + " limit: " + str(limit) + " exceedsLimit: " + str(answer_queries(nums, queries, limit)))

