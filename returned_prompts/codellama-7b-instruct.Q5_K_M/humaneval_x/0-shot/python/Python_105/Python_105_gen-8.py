
    def by_length(arr):
        # sort the array
        arr = sorted(arr)
        # reverse the array
        arr = arr[::-1]
        # create a list of strings
        # ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        name_list = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        # create an empty list
        answer = []
        # loop through array and append the name to the answer list
        for i in arr:
            if i >= 1 and i <= 9:
                answer.append(name_list[i - 1])
            else:
                answer.append(str(i))
        # return the answer list
        return answer
