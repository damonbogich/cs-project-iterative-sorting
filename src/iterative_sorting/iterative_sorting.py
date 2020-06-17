# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    
    #looping through indexes
    for i in range(0, len(arr) ):

        #steps:
        # 1. set current index to first index
        # 2. set smallest index to current index
        current_index = i
        smallest_index = current_index

        # TO-DO: swap
        # Your code here

        # 3. compare smallest index to the rest of the list until 
        # smaller value is found

        # ? how do i compare the first item in the list to the rest of the list until
        #smaller value is found
        #try looping through the rest of the list and comparing the values to smallest
        for j in range(i + 1, len(arr) ):
            #check if each value is greater than smallest index 
            compare_index = j
            #does loop just iterate again if following if statement is not true?
            #assuming yes for now
            if arr[compare_index] < arr[smallest_index]:
               
                smallest_index = compare_index 
                
        smallest_value = arr[smallest_index]
        current_value = arr[current_index]

        arr[current_index] = smallest_value
        arr[smallest_index] = current_value
        

    return arr







# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # first we want to compare the first and second items in the array
    swap = True
    #1. for loop through list
    while swap is True:
        swap = False
        for i in range(0, len(arr) - 1):
        #2. set current index to a variable
            current_index = i
        # compare arr[current_index] to the next value in array
            if arr[current_index] > arr[current_index + 1]:
                arr[current_index], arr[current_index + 1] = arr[current_index + 1], arr[current_index]

                swap = True
            # else: 
            #     swap = False
        
            
                

    return arr













    

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
