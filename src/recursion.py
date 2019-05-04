# simple recursion
def length_1(array):
    if array == []:
        return 0
    return 1 + length_1(array[1:])

# Tail recursion
def length_2(array):
    return length_3(array, 0)

def length_3(array, acc):
    if array == []:
        return acc
    else :
        acc +=1 
        return length_3(array[1:],acc)


my_list = [1,2,3,4,5,6,7]
print(length_1(my_list))
print(length_2(my_list))