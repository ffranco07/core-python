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

 Given a binary string s (containing only "0" and "1"). 
 You may choose up to one "0" and flip it to a "1". 
 What is the length of the longest substring achievable 
 that contains only "1"?
 
 For example, given s = "1101100111", the answer is 5. 
 If you perform the flip at index 2, the string becomes 
 1111100111.

"""

# Function to find longest substring only 1's after 0 flipped to 1
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_longest_substring_only_1s(s):
     # curr is the current number of zeros in the window
    left = curr = ans = 0 
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1
        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

s = "1101100111"
print("Orig: " + str(s)  + " longestSubstringOnly1s: " + str(find_longest_substring_only_1s(s)))

