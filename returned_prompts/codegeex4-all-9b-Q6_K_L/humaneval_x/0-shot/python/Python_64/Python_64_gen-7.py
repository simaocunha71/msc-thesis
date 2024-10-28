
def vowels_count(s):
    return sum(1 for x in s if x in 'aeiouAEIOU' or (x == 'y' and s[-1] == 'y'))