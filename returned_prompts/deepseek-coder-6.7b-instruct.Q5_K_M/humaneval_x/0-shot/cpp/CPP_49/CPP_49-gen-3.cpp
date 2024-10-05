    if(n==0)
        return 1;
    else
        return (2*modp(n-1,p))%p;
}
int main(){
    int n,p;
    scanf("%d%d",&n,&p);
    printf("%d\n",modp(n,p));
    return 0;
}
```

In this code, we defined a function `modp(int n,int p)`, which takes two integer arguments `n` and `p`. It will return the result of `2^n` modulo `p`. The function uses recursion to calculate the power. If `n` is zero, it returns 1 (as any number to the power of 0 is 1). Otherwise, it multiplies 2 with the result of `modp(n-1,p)` and returns the modulo of `p`. This process repeats until `n` is zero.

We then call this function in the `main()` function with the user input values of `n` and `p`, and print the result.

The code does not handle the case where `p` is 1, as the modulo of any number by 1 is always 0.

Please note that this code will not work as expected if `n` is negative, as the power operation is not defined for negative bases.

To handle negative `n`, you would need to first calculate `2^(-n)` and then take the reciprocal modulo `p`. This can be done with the `invmodp` function, which calculates the multiplicative inverse of a number modulo `p`.

Finally, the code does not handle the case where `n` is very large, as the recursion depth will be too high. To handle large `n`, you would need to implement a loop-based solution instead of recursion.

Also, note that this code will not work as expected if `p` is less than or equal to 1, as the modulo operation is not defined for these values.

Please note that this code will not work as expected if `n` is negative, as the power operation is not defined for negative bases.

To handle negative `n`, you would need to first calculate `2