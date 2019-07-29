array = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
child = [[] for _ in range(len(array))]

def height(array):
    if not array:
        return 1
    print(array)
    if len(array) ==1:
        return 1 + height(child[array[0]])
    else:
        return 1 + max(height(child[array[0]]),height(child[array[1]]))

def tree(array):
    for i, el in enumerate(array):
        child[el].append(i) if el!=-1 else ''
    print(child)
    result = [height(child[array.index(-1)]) for i in range(len(child))]
    print(result)
    return(max(result))
