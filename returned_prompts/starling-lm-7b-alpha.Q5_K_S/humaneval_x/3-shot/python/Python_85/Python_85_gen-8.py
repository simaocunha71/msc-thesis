    even_odds = []
    for i in range(0,len(lst),2):
        if lst[i] % 2 == 0:
            even_odds.append(lst[i])
    return sum(even_odds)


