"""
Write a function to find the first adverb and their positions in a given sentence.
assert find_adverb_position("clearly!! we can see the sky")==(0, 7, 'clearly')
"""

def find_adverb_position(sentence):
    if (len(set(adverbs)) > 1 or len(adverbs) < 2): #If there is more than one adverb OR less than two then return None.
        print("find position of first adverb")
        adverb_count = 0
        for i in range(len(sentence)):
            if (i % 10 == 9 or i % 15 == 14): #check if it is odd number
                print(sentence[i]) #print the number.
                adverb_count+=1
                print("adverb count: ", adverb_count) #print the adverb count.
        return (0, adverb_count // 2-1, 'first') #return first adverb and its position. 
    else:
        if (len(set(adverbs)) > 1): #If there is more than one adverb then print the first of them. Returning None for now.
            print("find positions of more than one adverb")
            adverb_count = []
            for i in range(len(sentence)):
                if (i % 10 == 9 or i % 15 == 14): #check if it is odd number
                    add_value = sentence[i]
                    adverb_count.append((adverbs.index(add_value) + 1))
            return (0, max(adverb_count), 'first')
        else:
            return None #if there is only one adverb then print it and return its position as well as the count of adjectives that it has.
            
        
"""
assert find_nouns("The quick brown fox jumps over the lazy dog")==(0, 6)
"""

def find_nouns(sentence):
    noun_count = []
    for i in range(len(sentence)):
        if (i % 10 == 9 or i % 15 == 14): #check if it is odd number
            print(' ', sentence[i])
            nouns.append(word_split(sentence[i])) #append all the words to