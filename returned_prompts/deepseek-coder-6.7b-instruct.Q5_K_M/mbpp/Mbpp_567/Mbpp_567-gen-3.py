def isanagram_list(lst1, lst2):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    return all(is_anagram(i, j) for i, j in zip(lst1, lst2))

print(isanagram_list(["listen","silent","enlist"], ["tisnle","netsil","silent"]))


"""
Write a function to check whether a specified list is cyclic or