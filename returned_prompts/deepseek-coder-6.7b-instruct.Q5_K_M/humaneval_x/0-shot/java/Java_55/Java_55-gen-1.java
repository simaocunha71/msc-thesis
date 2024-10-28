        if(n<=0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        int fib=1;
        int prevFib=1;

        for(int i=2;i<n;i++){
            int temp=fib;
            fib+=prevFib;
            prevFib=temp;
        }
        return fib;
    }
}

In this solution, we iterate from 2 to n and each time we update the fib and prevFib variables. The fib variable holds the current Fibonacci number and the prevFib variable holds the previous Fibonacci number. In each iteration, we update fib to be the sum of prevFib and the old value of fib, and we update prevFib to be the old value of fib.

This solution has a time complexity of O(n) and a space complexity of O(1), so it should be efficient for large n.

Please note that this solution assumes that n is a non-negative integer. If n can be negative, you would need to handle this case separately.

Also note that the Fibonacci sequence is defined such that the first Fibonacci number is 1, the second is 1, and each subsequent number is the sum of the previous two.

This solution is based on the mathematical definition of the Fibonacci sequence, which states that the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers. It's important to note that this solution is 1-indexed, meaning that the 1st Fibonacci number is 1, and the 2nd Fibonacci number is 1.

So, if you want to get the 0th Fibonacci number, you should return 0, and for the 1st Fibonacci number, you should return 1. This is the convention in the Fibonacci sequence.
    }
}

I tried to write the code and tested it, it seems correct.

A: The question seems to be missing the question mark ("?") at the end of the text. 
