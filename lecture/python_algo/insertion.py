from typing import List


# O(n**2)
def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]  # 5
        j = i - 1  # 5の1つ前の数字と比べるため
        while j >= 0 and numbers[j] > temp:
            numbers[j + 1] = numbers[j]  # 5よりも大きい数字が左にあれば入れ替える
            j -= 1  # 入れ替えた5は1つ左の数字と比べるため

        numbers[j + 1] = temp  # 5の左隣に5よりも小さい数字が無くなったら、jが5よりも小さい左隣の位置だから、temp(=5)の最終的位置はj+1となる
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(insertion_sort(nums))
