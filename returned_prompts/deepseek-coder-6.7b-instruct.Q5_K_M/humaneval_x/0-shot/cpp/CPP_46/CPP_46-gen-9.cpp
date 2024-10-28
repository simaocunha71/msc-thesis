    if(n<=3)
        return n==0?0:2;
    int a=0, b=0, c=2, d=0, e;
    for(int i=4; i<=n; i++){
        e = a + b + c + d;
        a = b;
        b = c;
        c = d;
        d = e;
    }
    return e;
}
int main(){
    printf("%d\n", fib4(5));  // prints: 4
    printf("%d\n", fib4(6));  // prints: 8
    printf("%d\n", fib4(7));  // prints: 14
    return 0;
}

Explanation:
The function `fib4` starts with four base cases to handle the first four numbers in the sequence. If `n` is less than or equal to 3, it returns `0` if `n` is `0` and `2` if `n` is `2` or `3`.

For `n` greater than 3, it computes the sequence iteratively. It keeps track of the last four numbers in the sequence in variables `a`, `b`, `c` and `d`. The current number `e` is computed as the sum of these four numbers. The variables are then updated to keep track of the last four numbers in the sequence for the next iteration. 

The function returns `e` which is the `n-th` number in the fib4 sequence.
*/

