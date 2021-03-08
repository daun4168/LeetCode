# Given a string s, find the length of the longest substring without repeating c
# haracters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  Example 4: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table Two Pointers String Sliding Window 
#  👍 13364 👎 690


# leetcode submit region begin(Prohibit modification and deletion)

# O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len_substring = 0
        for st_idx in range(len(s)):
            ch_set = set()
            ch_set.add(s[st_idx])

            end_idx = st_idx + 1
            while end_idx < len(s):
                if s[end_idx] in ch_set:
                    break
                else:
                    ch_set.add(s[end_idx])
                end_idx += 1

            max_len_substring = max(max_len_substring, end_idx - st_idx)

        return max_len_substring


# O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st_idx = 0
        end_idx = 0
        ch_dict = dict()

        max_len_substring = 0

        while end_idx < len(s):
            if s[end_idx] in ch_dict:
                st_idx = max(ch_dict[s[end_idx]] + 1, st_idx)

            max_len_substring = max(max_len_substring, end_idx - st_idx + 1)
            ch_dict[s[end_idx]] = end_idx

            end_idx += 1

        return max_len_substring

        
# leetcode submit region end(Prohibit modification and deletion)
