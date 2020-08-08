
# ? O(n)

def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        


    return -1   # not found


# * Write an iterative implementation of Binary Search
# ? - O(log n)

def binary_search(arr, target):

    # Your code here
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            # search to the right
            right = middle - 1
        else:
            # search to the left
            left = middle + 1


    return -1  # not found
