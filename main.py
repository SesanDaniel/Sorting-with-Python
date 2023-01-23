def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


arr = [3, 7, 9, 2, 16, 22, 11, 4, 8, 1, 14]
print(bubble_sort(arr))
