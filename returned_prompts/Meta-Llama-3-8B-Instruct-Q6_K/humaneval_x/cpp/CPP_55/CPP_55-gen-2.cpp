    if(n <= 1)
        return n;
    else
        return fib(n-1)+fib(n-2);

}
int main(){
    int n;
    printf("Enter the number of terms: ");
    scanf("%d",&n);
    printf("The %dth Fibonacci number is: %d\n",n,fib(n));
    return 0;
}

```
This is a recursive implementation of the Fibonacci sequence, which is not efficient for large values of n. It has a time complexity of O(2^n), which can cause a stack overflow for large values of n.

In the main function, you are taking input from the user for the number of terms in the Fibonacci sequence, and then calling the fib function to calculate the nth Fibonacci number.

However, this implementation is not suitable for large values of n because it has a high time complexity. For large values of n, you should use an iterative approach or a memoized recursive approach to calculate the Fibonacci number.

Here is an example of an iterative implementation of the Fibonacci sequence:

```c
int fib(int n) {
    if(n <= 1)
        return n;
    int a = 0, b = 1;
    for(int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}
```

This implementation has a time complexity of O(n) and is suitable for large values of n. You can use this implementation in your main function to calculate the nth Fibonacci number.