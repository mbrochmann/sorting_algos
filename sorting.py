from random_words import *
from insertion_sort import *
from bubble_sort import *
from merge_sort import *


def run_insertion_sort(list_length=3, save_string=""):

    words_list = random_words_list(list_length, save_string)

    print("")
    for i in range(0,len(words_list)):
        print("%i: %s" % (i, words_list[i]))

    #bubble_sort(words_list)
    #sorted_words_list = merge_sort(words_list)
    insertion_sort(words_list,10,19)

    print("")
    for i in range(0,len(words_list)):
        print("%i: %s" % (i, words_list[i]))

    #random_word = get_random_word()

    #print("")
    #print("Inserting word: %s" % random_word)
    #print("")

    #bisection_insert(random_word,sorted_words_list)

    #for i in range(0,len(sorted_words_list)):
        #print(sorted_words_list[i])
    #print("")


if(len(sys.argv)==3):
    run_insertion_sort(int(sys.argv[1]),sys.argv[2])
elif(len(sys.argv)==2):
    run_insertion_sort(int(sys.argv[1]))
else:
    run_insertion_sort()



#words_list_0 = random_words_list(-1, "random_words_20_a")
#words_list_1 = random_words_list(-1, "random_words_20_b")

#insertion_sort(words_list_0)
#insertion_sort(words_list_1)

#print(words_list_0)
#print(words_list_1)

#print(merge(words_list_0,words_list_1))


