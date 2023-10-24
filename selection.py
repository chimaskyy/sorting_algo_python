def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

arr = [5, 8, 0, 3, 1, 1, 9, 4]
print(arr)
selectionSort(arr)
print(arr)