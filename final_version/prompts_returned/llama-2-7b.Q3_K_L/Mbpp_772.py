"""
Write a function to remove all the words with k length in the given string.
assert remove_length('The person is most value tet', 3) == 'person is most value'
"""
def remove_length(word,k):
    # write your code here
    flag = True
    for i in range (len(word)):
        if(i>len(word)-k-1 and word[i] != ' ') :
            flag=False
            break;
    print("flag",flag)
    return  list(filter(lambda x: x not in [' ', '-'],word.split())) if (flag==True) else []
