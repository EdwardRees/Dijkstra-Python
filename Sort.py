def sort(arr):
    """
    Sorts a arr
    """
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if(arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
