class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        for open_bracket, close_bracket in zip(open_brackets, close_brackets):
            idx = s.find(open_bracket)
            open_bracket_idx = []
            while idx != -1:
                open_bracket_idx.append(idx)
                idx = s.find(open_bracket, idx+1)
            for idx in open_bracket_idx:
                if s[idx+1] == close_bracket:
                    return True
                else:
                    return False

# open_bracketsがあるインデックス位置を特定する
# 特定したopen_bracketsの位置より右にclose_bracketsがあるか確認
# あればtrue,　なけらばfalse

sol = Solution()
s = '{()}'
result = sol.isValid(s)
print(result)
