from typing import List


# O(n**2)
def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i
        for j in range(i + 1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
    return numbers


if __name__ == '__main__':
    import random
    import time
    nums = [random.randint(0, 1000) for _ in range(100)]

    start = time.time()
    r = sorted(nums) # 配列要素が増えるほど、sorted関数のほうが早い
    sorted_time = time.time() - start

    start = time.time()
    r = selection_sort(nums)
    selection_sort_time = time.time() - start


    print(sorted_time)
    print(selection_sort_time)
