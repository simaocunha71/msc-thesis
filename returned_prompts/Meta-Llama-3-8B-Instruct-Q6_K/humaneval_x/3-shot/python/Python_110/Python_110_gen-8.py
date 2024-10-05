    for num in lst1:
        if num % 2 != 0:
            for num2 in lst2:
                if num2 % 2 == 0:
                    lst1.remove(num)
                    lst2.remove(num2)
                    lst1.append(num2)
                    lst2.append(num)
                    return "YES"
    return "NO"


