    def solve(lst):
        string1 = lst[0]
        string2 = lst[1]
        if len(string1) != len(string2):
            return "No"

        count1 = 0
        count2 = 0
        for i in range(len(string1)):
            if string1[i] == '(':
                count1 += 1
            if string1[i] == ')':
                count1 -= 1
            if string2[i] == '(':
                count2 += 1
            if string2[i] == ')':
                count2 -= 1
            if count1 < 0 or count2 < 0:
                return "No"
        if count1 != 0 or count2 != 0:
            return "No"
        return "Yes"

    return solve(lst)


