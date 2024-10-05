    int fibfibNums[3] = {0, 0, 1};
    if(n < 3){
        return fibfibNums[n];
    }

B:
    for(int i = 3; i <= n; i++){
        int nextNum = fibfibNums[0] + fibfibNums[1] + fibfibNums[2];
        fibfibNums[0] = fibfibNums[1];
        fibfibNums[1] = fibfibNums[2];
        fibfibNums[2] = nextNum;
    }

C:
    return fibfibNums[2];
}

int main(){
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));
    return 0;
}
```

**Explanation**

The function `fibfib(n)` calculates the n-th number in the fibonacci series. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. The FibFib sequence, on the other hand, is defined such that a number is the sum of the last three numbers.

The function starts by initializing an array `fibfibNums` with the first three numbers of the sequence (0, 0, and 1).

The function then enters a loop that starts from 3 and goes up to `n`. In each iteration of the loop, it calculates the next number in the sequence by adding the last three numbers in the `fibfibNums` array. It then shifts the last three numbers in the `fibfibNums` array one place to the left to keep track of the last three numbers.

Finally, the function returns the last number in the `fibfibNums` array, which is the n-th number in the fibonacci sequence.

The `main()` function is used to test the `fibfib(n)` function.

**Time complexity**

The time complexity