
    def count_chars(lst):
        count = 0
        for word in lst:
            count += len(word)
        return count

    count1 = count_chars(lst1)
    count2 = count_chars(lst2)

    if count1 < count2:
        return lst1
    elif count2 < count1:
        return lst2
    else:
        return lst1