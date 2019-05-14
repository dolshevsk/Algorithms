def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):

    result = []
    left_index = right_index = 0
    
    while left_index < len(left) and right_index < len(right):

        if left[left_index] > right[right_index]:
            result.append(left[left_index])
            left_index +=1
        
        else:
            result.append(right[right_index])
            right_index += 1
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result



mylist = [12,8,7]
print(merge_sort(mylist))



