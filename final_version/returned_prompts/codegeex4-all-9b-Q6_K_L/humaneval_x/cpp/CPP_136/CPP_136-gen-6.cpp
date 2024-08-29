def largest_smallest_integers(lst):
    negative = []
    positive = []
    for i in lst:
        if i < 0:
            negative.append(i)
        elif i > 0:
            positive.append(i)
    if negative == []:
        negative.append(0)
    if positive == []:
        positive.append(0)
    return [max(negative), min(positive)]
