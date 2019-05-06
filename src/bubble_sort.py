def bubble_sort(array):
    swaped = True
    while swaped:
        swaped = False
        for i in range(len(array)-1):
                if array[i] < array[i+1]:
                        array[i], array[i+1]  = array[i+1], array[i]
                        swaped = True
    return array

my_list = [4,5,6,23,12,4,31,1,0]
print(bubble_sort(my_list))
        