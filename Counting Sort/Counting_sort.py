def countingSort(arr):
    count = [0] * 100
    for i in range(0,len(arr)):
        count[arr[i]] += 1  
    return count