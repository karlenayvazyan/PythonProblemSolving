import unittest
from src.longest_substring import Solution

class testSolution(unittest.TestCase):

    def test_0(self):
        result = Solution().lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, result)

    def test_1(self):
        result = Solution().lengthOfLongestSubstring("bbbbb")
        self.assertEqual(1, result)

    def test_3(self):
        result = Solution().lengthOfLongestSubstring(" ")
        self.assertEqual(1, result)

    def test_4(self):
        result = Solution().lengthOfLongestSubstring("au")
        self.assertEqual(2, result)

    def test_5(self):
        result = Solution().lengthOfLongestSubstring("aab")
        self.assertEqual(2, result)

    def test_2(self):
        result = Solution().lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, result)

    def test_6(self):
        result = Solution().lengthOfLongestSubstring("dvdf")
        self.assertEqual(3, result)
