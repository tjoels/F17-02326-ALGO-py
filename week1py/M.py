# week1 assignment M
A = [1, 3, 7, 15, 17, 11, 2, 3, 6, 8, 7, 5, 9, 5, 23, 2]
def arrayFun(A):
    x = 0
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            for k in range(j + 1, len(A)):
                x += 1
                if A[i] + A[j] + A[k] == 0:
                    print("hi")
    print(x)
arrayFun(A)