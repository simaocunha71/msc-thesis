def sum_prime(start, end):
    def prime_num(n):
        if n<2:
            return False
        if n==2 or n==3:
            return True
        if n%2==0 or n%3==0:
            return False
        i=5
        while i*i<=n:
            if n%i==0 or n%(i+2)==0:
                return False
            i+=6
        return True
    return sum(i for i in range(start, end+1) if prime_num(i))

print(sum_prime(1,10)) # 17

# OR

def sum_prime(start, end