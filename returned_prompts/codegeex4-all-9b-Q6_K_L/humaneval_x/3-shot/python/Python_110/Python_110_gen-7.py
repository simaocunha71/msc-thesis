    for num in lst1:
        if num % 2 == 1:
            for num2 in lst2:
                if num2 % 2 == 0:
                    lst1.remove(num)
                    lst1.append(num2)
                    lst2.remove(num2)
                    lst2.append(num)
                    break
            else:
                return "NO"
    return "YES"

