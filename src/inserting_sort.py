def insertion_sort(array):  
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > item_to_insert:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = item_to_insert
    
    return array

my_list = [4,5,6,23,12,4,31,1,0]
print(insertion_sort(my_list))