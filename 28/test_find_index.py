import unittest
import find_index


class CalTest(unittest.TestCase):
    def test_strStr1(self):
        sol = find_index.Solution()
        haystack = "sadbutsad"
        needle = "sad"
        self.assertEqual(sol.strStr(haystack, needle), 0)


    def test_strStr2(self):
        sol = find_index.Solution()
        haystack = "leetcode"
        needle = "leeto"
        self.assertEqual(sol.strStr(haystack, needle), -1)


if __name__ == "__main__":
    unittest.main()
