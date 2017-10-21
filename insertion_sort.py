from urllib import urlopen
import unirest
import json
import sys


def bisection_insert_0(entry, list, index_low=0, index_high=-2, offset_odd=1):
    """
    Original, not recursive
    Returns the index where the entry was inserted

    """
    if (index_high==-2):
        index_high = len(list)-1
        index_low = 0
    index_bisector = (index_high+index_low+offset_odd) // 2
    while (index_high >= index_low):
        if entry < list[index_bisector]:
            index_high = index_bisector-1
        else:
            index_low = index_bisector+1
        index_bisector = (index_high+index_low+offset_odd) // 2
    #list.insert(index_bisector+1-offset_odd,entry)
    #same as
    #list.insert(index_high+1,entry)
    #or
    list.insert(index_low,entry)
    return(index_low)

def bisection_insert(entry, list, index_low=0, index_high=-2, offset_odd=1):
    """
    Recursive, just for fun
    Returns the index where the entry was inserted

    """
    if (index_high==-2):
        index_high = len(list)-1
        index_low = 0
    index_bisector = (index_high+index_low+offset_odd) // 2
    #print("index_high: %i" % index_high)
    #print("index_low: %i" % index_low)
    #print("index_bisector: %i" % index_bisector)
    #print("inserting: %s" % entry)
    if (index_high >= index_low):
        if entry < list[index_bisector]:
            index_high = index_bisector-1
        else:
            index_low = index_bisector+1
        return(bisection_insert(entry, list, index_low, index_high, offset_odd))
    else:
        list.insert(index_low,entry)
        return(index_low)

def insertion_sort_0(random_words):
    """
    Writes into a new list

    """
    sorted_words = []
    sorted_words.append(random_words[0])

    for i in range(1,len(random_words)):
        bisection_insert(random_words[i],sorted_words)
        #print(i)
        #print(sorted_words)

    return sorted_words


def insertion_sort(words_list, index_low=0, index_high=-2):
    """
    Writes into the same list
    Returns a list of the original indices of the current entries

    """
    origin = range(0,len(words_list))

    if (index_high==-2):
        index_high = len(words_list) - 1

    for i in range(index_low+1,index_high+1):
        #print(i)
        # note, index_high-1 is because we have popped off an element
        origin_index = bisection_insert(words_list.pop(index_high),words_list,index_low,i-1)
        #print(origin_index)
        origin.insert(int(origin_index),origin.pop(index_high))
        #bisection_insert(words_list.pop(i),words_list,index_low,i-1)
        #print(words_list)
        #print(origin)

    return origin


