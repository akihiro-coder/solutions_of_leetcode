class Solution:
    def has_same_element(self, chars):
        return all(char == chars[0] for char in chars)

    def longest_common_prefix(self, strs):
        if '' in strs:
            return ''

        if len(strs) == 1:
            return strs[0]
        
        common_prefix = ''
        shortest_str = min(strs, key=len)
        for i in range(len(shortest_str)):
            char_list = [s[i] for s in strs]
            if self.has_same_element(char_list):
                common_prefix += char_list[0]
            else:
                return common_prefix
        return common_prefix
                

strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
strs = ['ab', 'a']
strs = ['', '']
sol = Solution()
result = sol.longest_common_prefix(strs)
print(result)
