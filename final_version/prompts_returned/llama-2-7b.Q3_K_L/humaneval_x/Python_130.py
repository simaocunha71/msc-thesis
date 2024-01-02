
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """

    # Solution 1:
    def tribo():
        tmp = []
        for i in range (n+1):
            n_ = n - i 
            if n_ % 2 == 0:
                n_ += 1 / 2 
                tmp.append(1)
            else: 
                tmp.append(tribo()[i])
                for j in range (3):
                    tmp.append(tribo()[i+j + 1])
        return tmp

    print(tribo())
    
def levenshtein(n, m):
    """In this problem we'll calculate the Levenshtein distance between two words.
    The Levenshtein distance is defined as the number of symbols that can be 
    changed in one word to get the other word. The algorithm requires O(mn) time
    complexity, where n and m are length of first and second word respectively.
    
    A common example - In order to calculate Levenshtein distance between 'cats' 
    and 'dog', we