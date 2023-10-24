def maxHeapify(arr, root, heapSize):
    n = len(arr)
    left = 2 * root + 1
    right = 2 * root + 2
    largest = root

    if left < heapSize and arr[left] > arr[largest]:
        largest = left
    if right < heapSize and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        maxHeapify(arr, largest, heapSize)


def heapSort(arr):
    if len(arr) == 0:
        return
    n = len(arr)

    for i in range(n // 2 - 1, -1, - 1):
        maxHeapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, 0, i)

arr = [5, 8, 0, 3, 1, 1, 9, 4]
print(arr)
heapSort(arr)
print(arr)