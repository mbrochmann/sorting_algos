import math
from random_words import *


def get_left_child_index(index):
    return 2*index+1

def get_right_child_index(index):
    return 2*index+2

def has_left_child(index, N_elements):
    return bool(get_left_child_index(index) < N_elements)

def has_right_child(index, N_elements):
    return bool(get_right_child_index(index) < N_elements)

def get_parent_index(index):
    return (index-1) // 2

def get_level(index):
    return math.log(index+1,2) // 1

def is_leaf(index, N_elements):
    if (index > N_elements-1):
        raise ValueError('index greater than N_elements - 1')
    return (index > get_parent_index(N_elements-1))




def heapify(heap, index=0, N_elements=-1):
    if (N_elements == -1):
        N_elements = len(heap)
    if is_leaf(index, N_elements):
        return
    left_child_index = get_left_child_index(index)
    right_child_index = left_child_index + 1
    if (right_child_index==N_elements):
        # we have reached the last element, only compare left child
        if (heap[index] > heap[left_child_index]):
            # if current element is larger than left child, switch them
            heap[index], heap[left_child_index] = heap[left_child_index], heap[index]
        return

    # otherwise, first recursively heapify the child heaps
    # move this part outside and just iterate from last element that is not a leaf down to root
    # last non-leaf element is parent of last element
    # get_parent_index(N_elements-1) down to 0
    #heapify(heap, left_child_index, N_elements)
    #heapify(heap, right_child_index, N_elements)

    # umm not sure i am doing things in the right order
    # pretty sure i am :)

    if (heap[right_child_index] > heap[left_child_index]):
        # right_child is larger, so compare left_child with current element
        if (heap[index] > heap[left_child_index]):
            # if current element is larger than left_child, switch them
            heap[index], heap[left_child_index] = heap[left_child_index], heap[index]
            # and re-heaping the left_child may be necessary due to the new value at left_child
            heapify(heap, left_child_index, N_elements)
    else:
        # left_child is larger (or equal), so compare right_child with current element
        if (heap[index] > heap[right_child_index]):
            # if current element is larger than right_child, switch them
            heap[index], heap[right_child_index] = heap[right_child_index], heap[index]
            # and re-heaping the left_child may be necessary due to the new value at right_child
            heapify(heap, right_child_index, N_elements)

    return

heap = random_words_list(-1, "random_words_20_a") + random_words_list(-1, "random_words_20_b")

print(heap)

N_elements = len(heap)
# get_parent_index(N_elements-1) down to 0
#for i in range(get_parent_index(N_elements-1),0,-1):
for i in range(N_elements-1, -1, -1):
    
    heapify(heap, i, N_elements)

#heapify(heap) 

#print(heap)

for i in range(0, N_elements-2):
    print("%i: %s" % (i, heap[0]))
    heap[0] = heap.pop()
    heapify(heap)
print("%i: %s" % (N_elements-1, heap[0]))
heap.pop()

