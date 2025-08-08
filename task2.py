# Given a string s, find the length of the longest substring without repeating characters.
# Example
# Input: s = "bbbbb"
# Output: 1

# Input: s = "pwwkew"
# Output: 3

def lengthOfLongestSubstring(s):
    seen = set()
    start = 0
    max_len = 0

    for end in range(len(s)):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])
        max_len = max(max_len, end - start + 1)

    return max_len



print(lengthOfLongestSubstring("bbbbb")) 
print(lengthOfLongestSubstring("pwwkew")) 
