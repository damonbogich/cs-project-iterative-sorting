def linear_search(arr, target):
    #loop through array searching for target 
    # if target is found return the index of that target
    #if target is not found return -1

    # 1. loop through array by index
    for i in range(0, len(arr)):
        current_index = i
        if arr[current_index] == target:
            return current_index

    return -1
    
    # 2. search if any array index has value = target




    # return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # we have an ordered list and want to search it for a target item

    # Our first guess will directly in the middle of the array
    
    #if our first guess is correct we can return the index

    #if it is too high then we know that the middle index and all of the indices above it do not contain our item

    #if it is too low then we know middle index and all indices below it do not contain item

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = arr[middle]
        if guess == target:
            return middle
        if guess > target:
            #middle value is greater than target so get rid of middle and all values above it
            high = middle -1 
        if guess < target:
            low = middle + 1


    return -1  # not found
