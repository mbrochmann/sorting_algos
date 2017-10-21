from urllib import urlopen
import unirest
import json
import sys


def get_random_word():

    response = None
    random_word = ""
    # Need the following to handle timeouts 
    # and other wierd errors when consuming the words API
    while response is None:
        try:
            response = unirest.get("https://wordsapiv1.p.mashape.com/words/?random=true",
                                   headers={
                    "X-Mashape-Key": "y2CBc7g2rYmshZnT9V2esiqWwJVdp19MTPtjsndfOFw2UKF01a",
                    "Accept": "application/json"
                    }
                                   )
        except Exception, e:
            print str(e)
            continue
        
        try:
            random_word = response.body["word"]
        except Exception, e:
            print("Uh-oh!")
            print str(e)
            print("Spaghetti-oh!")
            print response.body
            print("Oh no!")
            response = None
            continue
    #print response.body
    return random_word


def random_words_list(list_length=3, save_string=""):

    random_words = []

    #print list_length
    #print save_string

    #print list_length == -1
    #print len(save_string) != 0

    if ((list_length == -1) & (len(save_string) != 0)):
        # We are not creating a new list, 
        # instead we read the list from save_string
        with open(save_string, "r") as f:
            for line in f:
                random_words.append(line.strip())

    elif list_length > 0:
        # We create a new list of random words
        for i in range(0,list_length):

            random_words.append(get_random_word())

            # If a save_string was passed, save the list of random words
            # to a file with that name
            if len(save_string) != 0:
                with open(save_string, "w") as f:
                    for w in random_words:
                        f.write(w + "\n")

    else:
        # We need to specify the list_length if we are not reading from a file
        raise ValueError('No file specified to read random_words from. \n' +
                         'First argument (list_length) must be positive.')

    #print random_words
    return random_words

