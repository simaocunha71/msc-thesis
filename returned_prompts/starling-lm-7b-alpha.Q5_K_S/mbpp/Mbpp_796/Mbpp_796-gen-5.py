def return_sum(d):
    summ = 0
    for i in d:
        summ += d[i]
    return summ

def test_return_sum():
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
test