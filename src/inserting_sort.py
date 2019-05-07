def insertion_sort(array):  
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(array)):
        item_to_insert = array[i]
        
        while i > 0 and array[i-1] < item_to_insert:
            array[i],array[i-1] = array[i-1], array[i]
            i -= 1
    
    return array

my_list = [4,5,6,23,12,4,31,1,0]
print(insertion_sort(my_list))