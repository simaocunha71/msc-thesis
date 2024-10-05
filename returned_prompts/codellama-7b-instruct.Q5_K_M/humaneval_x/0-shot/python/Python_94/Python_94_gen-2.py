

def skjkasdkd(lst):
    prime_list = []
    for i in lst:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return sum(map(int, str(max(prime_list))))