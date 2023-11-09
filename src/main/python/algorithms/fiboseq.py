"""
 Author: Francisco Franco
 
 Creates a series of numbers in which each number 
 (Fibonacci Number) is the sum of the two preceding numbers.

 f(n) = f(n-1) + f(n-2) for n > 1 and f(0) = 0 and f(1) = 1

"""

# Recursive function to calculate fibonacci sequence sum at n
# NOT AS EFFICIENT as iterative function below
#
# Top-down approach 
# Start from the top (the original problem) and move down toward the base cases
#
# Time Complexity: O(2^n) Upper Bound with Exponential Time
# Space Complexity: O(1)
def fibo_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

# Recursive function to calculate fibonacci sequence sum at n
# using dictionary/map memoization to avoid repeated recursive computations.
# When we find the answer (the return value) for a given 
# recursive step state, we cache that value in dictionary/map for resuse. 
#
# Top-down approach 
# Start from the top (the original problem) and move down toward the base cases
#
# Time Complexity: O(n) Upper Bound with Exponential Time
# Space Complexity: O(1)
def fibo_recursive_dp(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


# Iterative function to calculate fibonacci sequence sum at n
#
# Bottom-up approach 
# Start at the bottom (base cases) and work our way up to larger problems
#
# Time Complexity: O(n) Upper Bound with Exponential Time
# Space Complexity: O(1)
def fibo_iterative(n):
    arr = [0] * (n + 1)
    # base case - the second Fibonacci number is 1
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[n]

memo = {}
size = 6
print("size: " + str(size) + " fiboRecursive: " + str(fibo_recursive(size)))
print("size: " + str(size) + " fiboRecursiveDP: " + str(fibo_recursive(size)))
print("size: " + str(size) + " fiboIterative: " + str(fibo_recursive(size)))

