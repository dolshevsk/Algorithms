def binary_search(list, element):
    high = len(list) -1
    low = 0
    attempt = 0
    while low <= high:
        mid = (high + low)//2
        guess = list[mid]
        if element == guess:
            return f'element:{element} was found with {attempt} attempts'
        if element > guess:
            low = mid + 1
            attempt +=1
        if element < guess:
            high = mid -1
            attempt +=1  
    return f"{element} wasn't found"

my_list = [1,2,3,4,5,6,7,8,9,10]

print(binary_search(my_list, 5))
