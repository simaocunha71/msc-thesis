def count(lst):
    count = 0
    for i in lst:
        if i == True:
            count += 1
    return count

print(count([True,False,True]))

# Alternate Solution
def count(lst):
    return lst.count(True)

print(count([True,False,True]))

# Alternate Solution
def count(lst):
    return sum(lst)

print(count([True,False,True]))
<jupyter_output>
2
2
2
<jupyter_text>
Question 2
<jupyter_code>
