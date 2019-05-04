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

my_list = [4,5,6,23,12,4,31,1,0]
print(selecting_sort(my_list))

