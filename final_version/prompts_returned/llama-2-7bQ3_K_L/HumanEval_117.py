
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """

    if len(s) == 0:
        return []
    
    wordList = []   # the list of words in s containing exactly n consonants
        
    for c in s: # go through each character in string
      if (c.isalpha() and len(wordList)>0):
          while wordList[-1][-2] == ' ':
            wordList.pop() 
        print("Consonant: "+str(c))
        w = [c]+[i for i in s[:i+1] if i != " "]
        
        if len(w) < n: # there are less than n consonants, add it to the list
          wordList.append(w) 
        else : # word is already long enough
            break
    return wordList


if __name__=='__main__':
  print("Select Words Test")
  
  inp = ["Mary had a little lamb", "Uncle sam"]
    
  for e1,e2 in zip(inp,select_words(*[e1,str.strip(e1).lower()])):
      print("Input: "+str(e1))
      print("Output: "+ str(e2))