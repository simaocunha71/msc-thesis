"""
Write a function to count the pairs of reverse strings in the given string list. 
assert count_reverse_pairs(["julia", "best", "tseb", "for", "ailuj"])== 2
"""
from collections import Counter
def count_reverse_pairs(strlist):
    ret = defaultdict(int)
    for str in strlist:
        if len(str)-1 % 2 == 0:
            ret[len(str)]+=1
    return [f"{count} - {str}"] for count, str in Counter(strlist).items()
def main():
    print(count_reverse_pairs(['julia', 'best', 'tseb', 'for', 'ailuj']))

if __name__=="__main__": main()