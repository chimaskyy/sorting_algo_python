def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        control = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                control = True
        if control == False:
            break

arr = [5, 8, 0, 3, 1, 1, 9, 4]
print(arr)
bubbleSort(arr)
print(arr)