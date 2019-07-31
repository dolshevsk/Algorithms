# сортировка кучей, O(nlogn)
# basic func
def parent(i):
    return (i-1)//2
def right_child(i):
    return 2*i+2
def left_child(i):
    return 2*i+1

def sift_up(heap,i):
    while i!=0 and heap[i]>heap[parent(i)]:
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)

def sift_down(heap,i, size=None):
    swap_index = i
    size = size if size is not None else len(heap)-1
    
    while True: 
        left = left_child(i)
        right = right_child(i)

        if left<=size and heap[left] > heap[swap_index]:
            swap_index = left
        
        if right<=size and heap[right] > heap[swap_index]:
            swap_index = right
        
        if i != swap_index:
            heap[swap_index], heap[i] = heap[i], heap[swap_index]
            i = swap_index
        else:    
            break

def insert(heap,val):
    heap.append(val)
    sift_up(heap,len(heap)-1)
    
def extract_max(heap):
    size = len(heap)-1
    heap[0], heap[size] = heap[size], heap[0]
    result = heap.pop()
    sift_down(heap,0)
    return result

def remove(heap,i):
    heap[i] = float('inf')
    sift_up(heap,i)
    extract_max(heap)

def change_priority(heap,i,val):
    old = heap[i]
    heap[i] = val
    if val > old:
        sift_up(heap,i)
    else:
        sift_down(heap,i)

# heap_sort with space complexity O(n)
# almost same as inserting_sort but nlog(n) to extract max value
def heap_sort(array):
    heap = []
    result = []
    for val in array:
        insert(heap,val)
    print(heap)
    for _ in range(len(heap)):
        result.append(extract_max(heap))
    return result

# Inplace heap_sort without any space complexity 
# build_heap to create binary_heap from array
def build_heap(heap):
    for i in range(parent(len(heap)-2//2),-1,-1):
        sift_down(heap,i)
        
def heap_sort_inplace(heap):
    build_heap(heap)
    size = len(heap)-1
    for i in range(size,-1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_down(heap,0,i-1)



