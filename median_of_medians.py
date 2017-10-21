from insertion_sort import *

def partition5(list, index_low=0, index_high=-2, even_offset=0):
    """
    if list has an odd number of elements, returns index of median element
    if list has an even number of elements,
    if even_offset == 0, returns index of larger of the two median elements
    if even_offset == -1, returns index of smaller of the two median elements
    
    """
    if (index_high==-2):
        index_high = len(list) - 1
        length = index_high - index_low + 1
    if (length > 5):
        raise ValueError("partition5 requires list of length 5 or less")
    #origin = insertion_sort(list[index_low:index_high+1])
    #return origin[(length + even_offset) // 2]
    insertion_sort(list,index_low,index_high)
    return((length+even_offset) // 2)
    

def median_of_medians(list, index_low=0, index_high=-2, even_offset=0):
    if (index_high==-2):
        index_high = len(list) - 1
    length = index_high - index_low + 1

    if (length <= 5):
        return partition5(list,index_low,index_high,even_offset)

    for i in range(0,index_high+1,5):
        current_median_index = partition5(list,i,i+4,even_offset)
        



#testlist = [1,2,5,4,3]
#print(testlist[partition5(testlist[0:5],0)])
#print(testlist[partition5(testlist[0:5],-1)])
#testlist2 = [1,2,5,4]
#print(testlist2[partition5(testlist2[0:4],0)])
#print(testlist2[partition5(testlist2[0:4],-1)])

