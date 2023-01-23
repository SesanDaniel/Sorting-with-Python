def insertion_sort(arr):
    for i in range(1, len(arr)):
        ''' Assign the index to a temporary variable to give space for shifting'''
        tmp = arr[i]

        ''' Initialize another index holder for elements on the left side of the Ith index'''
        j = i - 1

        ''' Create a loop that runs if the Jth index is available i.e, Greater or equals to zero
         and the element in the Ith index is less than the element on the Jth index. While this loop runs,
         switch element on the Jth index by a step to fill the empty space vacated by the element
          on the Ith index'''
        while j >= 0 and tmp < arr[j]:
            arr[j + 1] = arr[j]

            '''decrement index J so it falls back to its previous position for continuous loop'''
            j -= 1

            '''Store the Ith index, previously moved to a temporary variable in the position where the 
            Jth index recently occupied'''
        arr[j + 1] = tmp


arr = [3, 6, 2, 9, 4, 1, 8, 7]
insertion_sort(arr)
print(arr)
