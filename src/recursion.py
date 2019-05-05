# simple recursion
def length_1(array):
    if array == []:
        return 0
    return 1 + length_1(array[1:])

# Tail recursion

def length_2(array, acc=0):
    if array == []:
        return acc
    else :
        acc +=1 
        return length_2(array[1:],acc)

def sum(array):
    if array == []:
        return 0
    return array[0] + sum(array[1:])

def max_val(array):
    if len(array)==1:
        return array[0]
    else:
        return max_val(array[1:]) if array[0]<=array[1] else max_val(array[:1] + array[2:])


my_list = [1,2,3,4,15,6,7]
print(length_1(my_list))
print(length_2(my_list))
print(sum(my_list))
print(max_val(my_list))