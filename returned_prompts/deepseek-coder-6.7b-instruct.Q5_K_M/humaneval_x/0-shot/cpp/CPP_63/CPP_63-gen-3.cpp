    if(n==0)
        return 0;
    if(n==1)
        return 0;
    if(n==2)
        return 1;
    int fib[n+1];
    fib[0] = 0;
    fib[1] = 0;
    fib[2] = 1;

B:
    for(int i=3; i<=n; i++){
        fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
    }

C:
    return fib[n];
}

int main(){
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));
    return 0;
}
```

## Efficient Approach

The given program is efficient because it uses dynamic programming to solve the problem. It stores the FibFib(i) for i in the range [0, n] in an array. This reduces the time complexity from O(n^2) to O(n), making it much faster for large inputs. 

The function begins by initializing the base cases (fibfib(0)=0, fibfib(1)=0, fibfib(2)=1). Then, it iterates from 3 to n, calculating the n-th FibFib number as the sum of the previous three FibFib numbers. Finally, it returns the n-th FibFib number. 

The main function is used to test the fibfib function with some inputs.

## Time Complexity

The time complexity of the program is O(n), where n is the input number. This is because the program only needs to iterate from 3 to n once, calculating each FibFib number as a sum of the previous three.

## Space Complexity

The space complexity of the program is also O(n), where n is the input number. This is because the program needs to store the FibFib numbers up to n in an array.

## Conclusion

The given program is an efficient solution to the problem. It uses dynamic programming to store previously