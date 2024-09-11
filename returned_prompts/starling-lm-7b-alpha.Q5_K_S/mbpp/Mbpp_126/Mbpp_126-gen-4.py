def sum_of_divisors(n1,n2):
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    return sum(list(set([i for i in range(1,min(n1,n2)+1) if n1%i==0 and n2%i==0])))
print(sum_of_divisors(10,15))
# Output: 6

def sum_of_divisors(n1,n2):
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    common_divisors = [i for i in range(1,min(n1,n2)+1) if n1%i==0 and n2%i==0]
    return sum(common_divisors)
print(sum_of_divisors(10,15))
# Output: 6

def sum_of_divisors(n1,n2):
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    common_divisors = set([i for i in range(1,min(n1,n2)+1) if n1%i==0 and n2%i==0])
    return sum(common_divisors)
print(sum_of_divisors(10,15))
# Output: 6

def sum_of_divisors(n1,n2):
    def gcd(a,b):
        while b:
            a,b=b,a%b
        return a
    common_divisors = {i for i in range(1,min(n1,n2)+1) if n1%i==0 and n2%i==0}
    return sum(common_divisors)
print(sum_of_divisors(10,15))
# Output: 6

def sum_of_divisors(n1,n2):
    def gcd(a,b):
        while b