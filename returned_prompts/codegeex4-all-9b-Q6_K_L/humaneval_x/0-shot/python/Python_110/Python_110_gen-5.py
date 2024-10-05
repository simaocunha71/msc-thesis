def exchange(lst1, lst2):
    # Determine the count of odd numbers in lst1
    odd_count = sum(1 for x in lst1 if x % 2 != 0)

    # Determine the count of even numbers in lst2
    even_count = sum(1 for x in lst2 if x % 2 == 0)

    # If the count of odd numbers in lst1 is less than or equal to the count of even numbers in lst2,
    # it is possible to exchange elements to make lst1 a list of only even numbers
    if odd_count <= even_count:
        return "YES"
    else:
        return "NO"