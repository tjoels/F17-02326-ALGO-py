"""
Implemented with the aid of
CLRS Chapter 2 insertion sort pseudo code.
A is an array that is to get sorted.
"""
def insertionSort(A):
    for index in range(1, len(A)):
        key = A[index]
        position = A[index - 1]

        #Insert  A[index] into sorted sequence A[1 .. index - 1].
        while position > 0 and position
