    if(n==0 || n==1){
        return 0;
    }
    else if(n==2){
        return 1;
    }
    else{
        int fibo[n+1];
        fibo[0] = 0;
        fibo[1] = 0;
        fibo[2] = 1;
        for(int i=3; i<=n; i++){
            fibo[i] = fibo[i-1] + fibo[i-2] + fibo[i-3];
        }
        return fibo[n];
    }
}

int main() {
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));
    return 0;
}


A: You are correct in the implementation. 

The problem with the question is that the sequence starts with 0, 0, 1 and then proceeds according to the formula given in the problem statement. It is not related to the standard Fibonacci sequence, which starts with 0 and 1 and each subsequent number is the sum of the two previous ones. 

So when you compute fibfib(5), it should return 4, not 2. The 5th element of the sequence is 4 (0, 0, 1, 1, 2, 4).

The code provided is correct. It computes the nth element of the extended Fibonacci sequence as you requested.

The time complexity of this implementation is O(n), and the space complexity is also O(n) due to the use of the fibo array. If you only cared about the nth number, you could optimize the space complexity to O(1) by only storing the last three numbers in the sequence.

The main function is used to test the fibfib function. It should print the numbers 0, 4 and 24 for n=1, 5 and 8 respectively.

In conclusion, this implementation is correct and efficient.


A: Here is the code in Python.
def fibfib(n):
    if n==0 or n==1