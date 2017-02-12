# Week1 assignment 5.1
def findMax():
    # A = [1, 3, 7, 15, 17, 11, 2, 3, 6, 8, 7, 5, 9, 5, 23]
    n = input()
    A = list(map(int, input().split()))
    max = 0
    for i in range(len(A)):
        if A[i] > A[max]:
            max = i
    print(max)
    return max
findMax()
