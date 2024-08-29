def find_Max_Num(lst):
    lst.sort(reverse=True)
    return int("".join(map(str, lst)))

print(find_Max_Num([1,2,3])) #== 321

#Another way
def find_Max_Num(lst):
    return int(''.join(sorted(map(str, lst), reverse=True)))

print(find_Max_Num([1,2,3])) #== 321

#Another way
def find_Max_Num(lst):
    lst = [str(i) for i in lst]
    lst.sort(reverse=True)
    return int("".join(lst))

print(find_Max_Num([1,2,3])) #== 321

#Another way
def find_Max_Num(lst):
    lst.sort(key = lambda x: str(x), reverse = True)
    return int("".join(map(str, lst)))

print(find_Max_Num([1,2,3])) #== 321
<jupyter_output>
321
321
321
321
<jupyter_text>
