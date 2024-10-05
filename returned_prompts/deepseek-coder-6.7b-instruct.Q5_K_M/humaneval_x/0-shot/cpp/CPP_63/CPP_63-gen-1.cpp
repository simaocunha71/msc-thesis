    if (n < 0)
        return -1;
    if (n == 0 || n == 1)
        return 0;
    if (n == 2)
        return 1;
B:
    int fibfib_n_minus_1 = 1;
    int fibfib_n_minus_2 = 0;
    int fibfib_n_minus_3 = 0;
    int fibfib_n = 0;
    for (int i = 3; i <= n; i++) {
        fibfib_n = fibfib_n_minus_1 + fibfib_n_minus_2 + fibfib_n_minus_3;
        fibfib_n_minus_3 = fibfib_n_minus_2;
        fibfib_n_minus_2 = fibfib_n_minus_1;
        fibfib_n_minus_1 = fibfib_n;
    }
    return fibfib_n;
}
int main(){
    int n;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The %d-th element of the fibfib number sequence is: %d\n", n, fibfib(n));
    return 0;
}
```

## Solution
This code calculates the n-th term of the FibFib sequence by iteratively applying the definition of the sequence. The value of each term is stored in the variables `fibfib_n_minus_1`, `fibfib_n_minus_2`, and `fibfib_n_minus_3`, which correspond to the n-1, n-2, and n-3 terms of the sequence, respectively. The variable `fibfib_n` is updated with the n-th term of the sequence in each iteration. The final value of `fibfib_n` is returned as the result.

The time complexity of this function is O(n), and the space complexity is O(1), since it only uses a constant amount of space to store the n-th term of the sequence and the previous three terms.

The program reads the value of n from