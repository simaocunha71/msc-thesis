def maximum(a, b):
    if(a > b):
        return a
    else:
        return b




# Python program to check if a number is prime or not

def isPrime(n) :
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True




def main():
    print(isPrime(13))

if __name__ == "__main__":
    main()





def find_max(a,b):
    if a > b:
        return a
    else:
        return b

def find_min(a,b):
    if a < b:
        return a
    else:
        return b

def find_abs(a,b):
    if a < b:
        return b - a
    else:
        return a - b

def find_gcd(a,b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

def find_lcm(a,b):
    return a * b / find_gcd(a, b)


if __name__ == "__main__":
    print(find_max(10, 14))
    print(find_min(10, 14))
    print(find_abs(10, 14))
    print(find_gcd(10, 14))
    print(find_lcm(10, 14))



















































