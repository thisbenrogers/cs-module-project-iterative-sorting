
# * Complete the selection_sort() function below
# ? - O(n²)

def selection_sort(arr):

    # * loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # * find next smallest element
        # * (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j



        # * swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# *  implement the Bubble Sort function below
# ? - O(n²)

def bubble_sort(arr):
    underway = True
    while underway:
        underway = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                underway = True
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

# ? What is the time and space complexity of the counting sort algorithm?
# ? 
# ?  - -  O(n + r) where 'r' is the range of positive integer key values 
# ? 
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return arr
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"

    maxxx = maximum + 1
    buckets = [0] * maxxx
    for i in arr:
        buckets[i] += 1
    tally = 0
    for i in range(maxxx):
        for j in range(buckets[i]):
            arr[tally] = i
            tally += 1
    return arr
