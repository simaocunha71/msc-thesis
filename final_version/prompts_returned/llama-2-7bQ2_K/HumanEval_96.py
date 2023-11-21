
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """

    prime = [2, 3, 5, 7, 11, 13]
    
    if n == 0: return []
    
    # loop until you get a number <= to the limit
    while n < len(prime):
        if prime[n] > 0 and is_prime(prime[n])):
            print(" ", prime[n])
            count_up_to(n - prime[n]+1) # decrement by one since you used prime[n] so subtract n-prime[n] from the while loop limit.
        else: 
            return [2,3,5,7,11,13]
            
    return []

if __name__ == "__main__":
    print(count_up_to(10))