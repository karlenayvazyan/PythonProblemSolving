class Solution:

    # "abcabcbb"
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        end = 0
        start = 0
        longest_length = 0
        char_set = {}
        while end < len(s) and start < len(s):
            cur = s[end]
            if cur in char_set:
                result = end - char_set[cur]
                longest_length = result if result > longest_length else longest_length
                char_set[s[end]] = end
            else:
                char_set[cur] = end
            end += 1

        return longest_length if longest_length > end else end
