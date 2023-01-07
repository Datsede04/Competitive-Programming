class Solution: 
    def select(self, arr, i):
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min =self.select(arr,i)
            for j in range(i+1,n):
                if min > arr[j]:
                    min = arr[j]
                    arr[j] = arr[i] 
                    arr[i] = min
            
        return arr   
            