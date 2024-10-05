    count = 0
    for i in nums:
        if (i > 10 and str(i)[0] == '1' and str(i)[-1] == '1') or (i > 10 and str(i)[0] == '3' and str(i)[-1] == '3') or (i > 10 and str(i)[0] == '5' and str(i)[-1] == '5') or (i > 10 and str(i)[0] == '7' and str(i)[-1] == '7') or (i > 10 and str(i)[0] == '9' and str(i)[-1] == '9'):
            count += 1
    return count


