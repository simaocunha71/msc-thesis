

def skjkasdkd(lst):
    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n%2 == 0:
            return False
        for i in range(3,int(n**0.5)+1,2):
            if n%i == 0:
                return False    
        return True

    prime_numbers = [i for i in lst if is_prime(i)]
    if len(prime_numbers) == 0:
        return 0
    largest_prime = max(prime_numbers)
    return sum(int(i) for i in str(largest_prime))


print(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])) #10
print(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])) #25
print(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])) #13
print(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6])) #11
print(skjkasdkd([0,81,12,3,1,21])) #3
print(skjkasdkd([0,8,1,2,1,7])) #7
<jupyter_output>
10
25
13
11
3
7
<jupyter_text>
Problem 28:
<jupyter_code>
