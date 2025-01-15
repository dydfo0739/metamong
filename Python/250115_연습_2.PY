def quick_sort(arr):
    """
    Quick Sort Algorithm
    :param arr: List of elements to sort
    :return: Sorted list
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":
    sample_array = [10, 7, 8, 1, 9, 3, 5, 2]
    print("Unsorted Array:", sample_array)
    sorted_array = quick_sort(sample_array)
    print("Sorted Array:", sorted_array)
