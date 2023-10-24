def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[j], arr[i] = arr[i],arr[j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):

    if low < high:
        part = partition(arr, low, high)
        quickSort(arr, low, part - 1)
        quickSort(arr, part + 1, high)

arr = [5, 8, 0, 3, 1, 1, 9, 4]
print(arr)
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)
