def selection_sort(arr):
    n = len(arr)

    for i in range(0, n - 1):
        min_num = i
        for j in range(i+1, n):
            if arr[min_num] > arr[j]:
                min_num = j
        temp = arr[i]
        arr[i] = arr[min_num]
        arr[min_num] = temp


arr = [3, 9, 4, 1, 7, 5, 2, 8]
selection_sort(arr)
print(arr)
