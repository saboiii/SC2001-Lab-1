import random
import time
import numpy as np
from typing import List, Tuple

comparison_count = 0


def reset_comparison_count():
    global comparison_count
    comparison_count = 0


def get_comparison_count():
    global comparison_count
    return comparison_count


def insertion_sort(arr: List[int], left: int, right: int) -> None:
    global comparison_count

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= left:
            comparison_count += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break

        arr[j + 1] = key


def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    global comparison_count

    n1 = mid - left + 1
    n2 = right - mid
    left_arr = [0] * n1
    right_arr = [0] * n2

    for i in range(n1):
        left_arr[i] = arr[left + i]
    for j in range(n2):
        right_arr[j] = arr[mid + 1 + j]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        comparison_count += 1
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def hybrid_mergesort(arr: List[int], left: int, right: int, threshold: int) -> None:
    if left < right:
        if right - left + 1 <= threshold:
            insertion_sort(arr, left, right)
        else:
            mid = (left + right) // 2
            hybrid_mergesort(arr, left, mid, threshold)
            hybrid_mergesort(arr, mid + 1, right, threshold)
            merge(arr, left, mid, right)


def original_mergesort(arr: List[int], left: int, right: int) -> None:
    if left < right:
        mid = (left + right) // 2
        original_mergesort(arr, left, mid)
        original_mergesort(arr, mid + 1, right)
        merge(arr, left, mid, right)


def generate_random_array(size: int, max_value: int = None) -> List[int]:
    if max_value is None:
        max_value = size * 10

    return [random.randint(1, max_value) for _ in range(size)]


def time_algorithm(sort_func, arr: List[int], *args) -> Tuple[float, int]:
    arr_copy = arr.copy()
    reset_comparison_count()

    start_time = time.perf_counter()

    if len(args) > 0:
        sort_func(arr_copy, 0, len(arr_copy) - 1, *args)
    else:
        sort_func(arr_copy, 0, len(arr_copy) - 1)

    end_time = time.perf_counter()

    return end_time - start_time, get_comparison_count()


if __name__ == "__main__":
    print("This module contains the core sorting algorithms.")
    print("Run 'python final-analysis.py' for the complete analysis.")
