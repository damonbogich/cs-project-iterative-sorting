def countdown_to_one(n):
    # 2. base case
    if n == 0:
        return

    print(n)
    countdown_to_one(n-1) # 1. calls itself


countdown_to_one(5)


#recursive sum:
def sum_list(items):
    # 1. base case
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[i:])  #2. recursive call
        # 3. moves twoards base case





# naive fibonacci:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

# we know the first two items are 0 and 1

# we know that every item in sequence is detrmined
# by summing the previous two items

def naive_fibonacci(n):
    #what is the base case?
    if n == 0:
        return 0
    if n == 1:
        return 1

    #what is the recursive case?
    
    #how does it move twoards the base case?



