    for num in lst1:
        if num % 2 != 0:
            for num2 in lst2:
                if num2 % 2 == 0:
                    lst1[lst1.index(num)] = num2
                    lst2[lst2.index(num2)] = num
                    break
            else:
                return 'NO'
    return 'YES'

