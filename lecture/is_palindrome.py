"""
1. Check palindrome(problem1)
aba => True
abc => False
racecar => True

2. Find palindrome(problem2)
abcracecarbda => cec, aceca, racecar
"""

# My solution

# solution1: reversed(sequence)やsliceを使う方法
# def is_palindrome(s: str) -> bool:
#     # reversed_s =  ''.join(reversed(s))
#     reversed_s = s[::-1]
#     if s == reversed_s:
#         return True


# solution1: reversed(sequence)やsliceを使わない方法
def is_palindrome(s: str) -> bool:
    length_s = len(s)
    loop_num = length_s // 2
    for i in range(loop_num):
        if s[i] != s[-i - 1]:
            return False
    return True


# Mr.Sakai's solution
# problem1
def is_palindrome(strings: str) -> bool:
    # 変数が空の文字列か判定
    len_strings = len(strings)
    if not len_strings:
        return False
    # 1文字ならばpalindrome
    if len_strings == 1:
        return True

    start, end = 0, len_strings - 1
    # 自分のコードよりも, index変数が１つ少ない分、forよりもwhileのコードのほうが処理の仕方が直感的にわかりやすい。
    while start < end:
        if strings[start] != strings[end]:
            return False
        start += 1
        end -= 1
    return True


# solution2: 中心から外側を調べていく
def find_palindrome(strings: str, left: int, right: int):
    result = []
    while 0 <= left and right <= len(strings) - 1:
        if strings[left] != strings[right]:
            break
        result.append(strings[left: right + 1])
        left -= 1
        right += 1
    return result


def find_all_palindrome(strings: str):
    result = []
    len_strings = len(strings)
    if not len_strings:
        return result
    if len_strings == 1:
        result.append(strings)

        # aba
        [result.append(s) for s in find_palindrome(strings, i-1, i+1)]
        # abba
    for i in range(1, len_strings - 1):
        [result.append(s) for s in find_palindrome(strings, i-1, i)]

    return result


if __name__ == '__main__':
    print(find_all_palindrome('cbabc'))
