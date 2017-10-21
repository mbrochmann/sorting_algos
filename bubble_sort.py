from urllib import urlopen
import unirest
import json
import sys


def bubble_sort(random_words):

    num_switches = -1
    
    # we need to sort through one less item each time,
    # since each iteration puts the last element in the actively sorted list at the end
    # in the worst case, the last sorting iteration will be on a list of two items
    for i in range(len(random_words),1,-1):
        if num_switches == 0:
            break
        num_switches = 0

        for j in range(0,i-1):
            
            if(random_words[j]>random_words[j+1]):
                random_words[j],random_words[j+1] = random_words[j+1],random_words[j]
                num_switches += 1
        
    return random_words
    

