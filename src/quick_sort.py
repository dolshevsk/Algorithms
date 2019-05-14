def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

my_list = [2,3,4,1,0,0,1,1,123, -1, 5]
print(quick_sort(my_list))