def highest_Power_of_2(n):
    p = 1
    while (p * 2 <= n):
        p *= 2
    return p




"""
def highest_Power_of_2(n):
    p = 1
    while (p * 2 <= n):
        p *= 2
    return p

def test_highest_Power_of_2():
    assert highest_Power_of_2(10) == 8

if __name__ == "__main__":
    test_highest_Power_of_2()
"""


"""
def highest_power_of_two(n):
    if (n == 0):
        return 0
    else:
        p = 1
        while(p < n):
            p *= 2
        return p

def main():
    n = int(input())
    print(highest_power_of_two(n))

if __name__ == "__main__":
    main()
"""
"""
def highest_power_of_two(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        p = 2
        while(p <= n):
            p *= 2
        return p

def main():
    n = int(input())
    print(highest_power_of_two(n))

if __name__ == "__main__":
    main()
"""
"""
def highest_power_of_two(n):
    if(n == 0):
        return 0
    else:
        if(n % 2 == 0):
            return n
        else:
            return n + 1

def main():
    n = int(input())
    print(highest_power_of_two(n))

if __name__ == "__main__":
    main()
"""
"""
def highest_power_of_two(n):
    p = 1
    while(p <= n):
        p *= 2
    return p

def main():
   