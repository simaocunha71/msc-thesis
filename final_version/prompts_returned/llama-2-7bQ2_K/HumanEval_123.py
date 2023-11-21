
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    
    return list(map(lambda x: x%2 != 0 , [i for i in range(n+3) if (i/2 < n or i==n)]))

def collatz_number(n):
    """
    Given a positive integer, print the number of Collatz numbers <= n. Where n is an odd number, print "odd" to denote that such even integers have not been considered in calculation of Collatz numbers. And when there are no more odd numbers, print -1 as return value.
    
    If the returned values is 0 or less than zero, then the caller should re-run the function with a higher value for n.
    """
    odd_collatzs = get_odd_collatz(n)
    count = 0
    for i in odd_collatzs:
        print("{} even".format(i), end="\t")
        
        if (count == 0):
            collatz_number=collatz_number(int(((i + int(.5 * i)) % (n+1)))) or -1
            break
            
        count+=1
    if (collatz_number < 