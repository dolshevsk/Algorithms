# средняя O(n2) 
# в лучшем случае О(n), когда список отсортирован
def insertion_sort(array):  
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    total = 0
    for i in range(1, len(array)):
        item_to_insert = array[i]
        
        while i > 0 and array[i-1] < item_to_insert:
            array[i] = array[i-1]
            i -= 1
            total +=1
        array[i]= item_to_insert
    print(f'make {total} totals')
    return array

my_list = [4,5,6,23,12,4,31,1,0]
my_list2 = [31,23,12,6,5,4,4,1,0]
print(insertion_sort(my_list))
print(insertion_sort(my_list2))