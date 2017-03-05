"""
Implemented with the aid of
CLRS Chapter 2 insertion sort pseudo code.
A is an array that is to get sorted.
"""
class InsertionSort:
    def insertionsort(A):
        for j in range(1, len(A)):
            key = A[j]
            #position = A[j - 1]

            #Insert  A[j] into sorted sequence A[1 .. j - 1].
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = key
        return A

''' Lines for debugging
A = [54,26,93,17,77,31,44,55,20]
#A = [15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
print(A)
print("Gets sorted with the result:")
insertionSort(A)
print(A)
'''