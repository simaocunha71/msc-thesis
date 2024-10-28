    def fib(n):
        """ Helper function to compute nth fibbonacci number """
        if n == 0 or n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n-1) + fib(n-2) + fib(n-3)

    return fib(n)


