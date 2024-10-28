def max_Abs_Diff(lst):
    if len(lst)<2:
        return "List should have at least two elements"
    else:
        max_dif=0
        for i in range(len(lst)):
            for j in range(i+1,len(lst)):
                max_dif=max(max_dif,abs(lst[i]-lst[j]))
        return max_dif