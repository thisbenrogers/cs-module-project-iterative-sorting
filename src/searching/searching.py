
# ? O(n)

def linear_search(arr, target):
    # Your code here
    for index, value in enumerate(arr):
        if value == target:
            return index
        


    return -1   # not found


# * Write an iterative implementation of Binary Search
# ? - O(log n)

def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
            continue
        high = mid


    return -1  # not found
