from typing import List


def partition(numbers: List[int], low: int, high: int) -> int:
    pass

# O(n*logn)
def quick_sort(numbers: List[int]) -> List[int]:
    def _quick_sort(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)




if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5, 7]
    print(quick_sort(nums))
