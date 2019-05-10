def bubble_sort(array):
    swaped = True
    while swaped:
        swaped = False
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                array[i], array[i+1]  = array[i+1], array[i]
                swaped = True
    return array

def cocktail_sort(array):
    left = 0
    right = len(array)-1

    while left <= right:
        for i in range(left, right,+1):
            if array[i] < array[i+1]:
                 array[i], array[i+1] = array[i+1], array[i]
        right -=1

        for i in range(right, left, -1):
            if array[i] > array[i-1]:
                 array[i], array[i-1] = array[i-1], array[i]
        left +=1
    return array



my_list = [4,5,6,23,12,4,31,1,0]
my_list_2 = [4,5,6,23,12,4,31,1,0]
print(bubble_sort(my_list))
print(cocktail_sort(my_list_2))
        