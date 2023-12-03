class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 見つかるか否か 見つからないとreturn -1
        # 見つかった場合の処理
        if needle not in haystack:
            return -1

        needle_length = len(needle)
        for idx_first_occurance in range(needle_length):
            if haystack[idx_first_occurance : idx_first_occurance + needle_length] == needle:
                return idx_first_occurance


sol = Solution()
needle = 'hello'
haystack = 'helloworld'
print(sol.strStr(haystack, needle))
