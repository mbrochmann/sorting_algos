from random_words import *
from insertion_sort import *

def merge(list0, list1):
    length0 = len(list0)
    length1 = len(list1)
    merged_list_final_length = length0 + length1
    merged_list = []
    index0 = 0
    index1 = 0
    merged_list_current_length = 0
    
    #print("")
    #print("Entering merge:")
    #print(list0)
    #print(list1)
    #print("---")

    while (merged_list_current_length < merged_list_final_length):

        if(index0 == length0):
            merged_list += list1[index1:length1]
            #print("Merged list:")
            #print(merged_list)
            #print("---")
            return merged_list

        if(index1 == length1):
            merged_list += list0[index0:length0]
            #print("Merged list:")
            #print(merged_list)
            #print("---")
            return merged_list

        if(list0[index0] < list1[index1]):
            merged_list.append(list0[index0])
            index0 += 1
        else:
            merged_list.append(list1[index1])
            index1 += 1
            
        merged_list_current_length += 1

    #print("Merged list:")
    #print(merged_list)
    #print("---")
    return merged_list


def merge_sort(words_list, offset_odd=1):
    #print("")
    #print("Entering merge_sort")
    index_high = len(words_list) - 1
    index_low = 0
    length = index_high - index_low + 1
    #print("index_low = %i" % index_low)
    #print("index_high = %i" % index_high)
    #print("length = %i" % length)
    #print(words_list[index_low:index_high+1])
    if(length < 2):
        #print("length < 2")
        #print(words_list[index_low:index_high+1])
        return words_list[index_low:index_high+1]
    else:
        index_bisector = (index_high+index_low-offset_odd) // 2
        list_0 = words_list[index_low:index_bisector+1]
        list_1 = words_list[index_bisector+1:index_high+1]
        #print("index_bisector = %s" % index_bisector)
        #print("list_0:")
        #print(list_0)
        #print("list_1:")
        #print(list_1)
        #print("About to sort and merge:")
        sorted_list_0 = merge_sort(list_0)
        sorted_list_1 = merge_sort(list_1)
        return merge(sorted_list_0, sorted_list_1)
                     
