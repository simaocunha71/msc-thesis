    # Write your code here.
    # You can use the following functions and methods:
    # len(), sum(), sorted(), max(), min(), append(), remove(), reverse(),
    # count(), index(), insert(), extend(), pop(), del, list

    if len(lst1) != len(lst2):
        return "NO"
    for i in lst2:
        if i%2==0 and i not in lst1:
            lst1.append(i)
    if all(i%2==0 for i in lst1):
        return "YES"
    return "NO"

``