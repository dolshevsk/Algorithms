def selecting_sort(array):
    sorted_list = []
    while array:
        max = array[0]
        max_index = 0
        for i in range(1, len(array)):
            if array[i] > max:
                max = array[i]
                max_index = i
        sorted_list.append(array.pop(max_index))
    return sorted_list

# without creating an empty list
def selecting_sort_2(array):
    for start_index in range(len(array)):
        max_index = start_index
        for i in range(start_index +1, len(array)):
            if  array[i] > array[start_index]:
                max_index = i
        print(array, start_index, max_index)
        array[start_index], array[max_index]= array[max_index], array[start_index]
    return array
                

my_list = [4,5,6,23,12,4,31,1,0]
print(selecting_sort_2(my_list))
print(selecting_sort(my_list))

