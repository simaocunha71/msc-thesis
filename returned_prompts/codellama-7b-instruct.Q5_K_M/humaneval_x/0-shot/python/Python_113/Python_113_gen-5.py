
def odd_count(lst):
    lst = [''.join(i) for i in lst]
    lst = [int(i) for i in lst]
    lst = [sum(i%2 for i in lst) for i in lst]
    lst = [str(i) for i in lst]
    lst = ['the number of odd elements ' + i + 'n the str' + i + 'ng ' + i + ' of the ' + i + 'nput.' for i in lst]
    return lst

