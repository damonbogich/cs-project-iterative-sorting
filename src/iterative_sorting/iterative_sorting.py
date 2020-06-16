# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    
    #looping through indexes
    for i in range(0, len(arr) - 1):

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
        for j in range(i + 1, len(arr) - 1):
            #check if each value is greater than smallest index 
            compare_index = j
            #does loop just iterate again if following if statement is not true?
            #assuming yes for now
            if arr[compare_index] < arr[smallest_index]:
                #then we want to set index of compare to value of smallest index
                
                
                smallest_index = compare_index #smallest_index = 7 
                #need to also put value of former smallest index to index 7
                #and we want arr[j] to compare to the remainder of the list
        # arr[compare_index] = arr[]
        
        arr[current_index] = arr[smallest_index]
        
        
                #how do i make sure that new smallest index now is picking up where
                #old smallest index left off????


            #trying to set up logic for when smallest index makes it to the end of list
            #want to set it to the first item of the list and then repeat the process
            
                # then we want to set smallest index to the first item in array

        # 4. if no smaller value is found then the first item in list should stay
        # at index 0
        # 5. if there is a smaller item found then current smallest index should swap
        # with that smaller value

        # 6. New smallest index goes through the if statements from steps 4 and 5

        # 7. When smallest item is found it is set to the first item in array 

        # 8. repeat process excluding the already set item in the array until all values 
        # are in order

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


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
