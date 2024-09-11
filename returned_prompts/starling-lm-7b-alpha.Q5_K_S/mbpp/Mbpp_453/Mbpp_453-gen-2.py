"""
def sumofFactors(n):
    result = 0
    for i in range(1,n+1):
        if(n%i == 0):
            if(i%2 == 0):
                result += i
    return result
"""

def sumofFactors(n):
    result = 0
    for i in range(1,n+1):
        if(n%i == 0):
            if(i%2 == 0):
                result += i
    return result


def test_sumofFactors():
    assert sumofFactors(18) == 26
    print("All Tests Passed")

test_sumofFactors()



```