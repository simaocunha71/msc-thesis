
    def odd_count(lst):
        result = []
        for i in range(len(lst)):
            temp = 0
            for j in range(len(lst[i])):
                if int(lst[i][j]) % 2 != 0:
                    temp += 1
            result.append(f"the number of odd elements {temp}n the str{temp}ng {i} of the {i}nput.")
        return result