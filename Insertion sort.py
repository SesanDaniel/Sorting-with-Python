def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and tmp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp


arr = [3, 6, 2, 9, 4, 1, 8, 7]
insertion_sort(arr)
print(arr)
