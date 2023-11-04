"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in 
non-decreasing order.

"""

# Function which sorts array after doing squares of elements
# Time Complexity: O(n)
# Space Complexity: O(n)
def sort_squares(arr, n):
    left, right = 0, n - 1
    index = n - 1
    result = [0 for x in arr]
 
    while index >= 0:
 
        if abs(arr[left]) >= abs(arr[right]):
            result[index] = arr[left] * arr[left]
            left += 1
        else:
            result[index] = arr[right] * arr[right]
            right -= 1
        index -= 1
     
    for i in range(n): 
        arr[i] = result[i]
 
# Driver code 
arr = [-6, -3, -1, 2, 4, 5 ] 
n = len(arr) 
 
print("Before sort ") 
for i in range(n): 
    print(arr[i], end =" " ) 
     
sort_squares(arr, n) 
print("\nAfter Sort ") 
for i in range(n): 
    print(arr[i], end =" " ) 