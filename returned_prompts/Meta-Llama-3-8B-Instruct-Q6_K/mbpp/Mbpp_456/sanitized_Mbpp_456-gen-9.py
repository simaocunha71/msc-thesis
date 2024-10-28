def reverse_string_list(lst):
    return [s[::-1] for s in lst] #using list comprehension and slicing to reverse each string
    #or
    #return [s[::-1] for s in lst] #using list comprehension and slicing to reverse each string
    #or
    #result = []
    #for s in lst:
    #    result.append(s[::-1])
    #return result