def binary_search(arr, target):
    """
    Binary Search Algorithm
    :param arr: Sorted list of elements
    :param target: Element to search for
    :return: Index of the target if found, else -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble_sort(arr):
    """
    Bubble Sort Algorithm
    :param arr: List of elements to sort
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def fibonacci(n):
    """
    Generate the nth Fibonacci number
    :param n: Position of the Fibonacci number to calculate
    :return: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def is_prime(num):
    """
    Check if a number is prime
    :param num: Number to check
    :return: True if prime, False otherwise
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
if __name__ == "__main__":
    print("Binary Search:", binary_search([1, 3, 5, 7, 9], 5))
    print("Bubble Sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))
    print("Fibonacci(10):", fibonacci(10))
    print("Is 29 Prime?:", is_prime(29))
