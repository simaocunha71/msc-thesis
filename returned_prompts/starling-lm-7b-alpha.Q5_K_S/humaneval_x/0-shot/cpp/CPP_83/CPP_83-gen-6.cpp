int a;
if (n == 1)
    return 1;
else if (n == 2)
    return 2;
else if (n == 3)
    return 3;
else
    return (9 * (n - 1) + 1);

}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d", starts_one_ends(n));
    return 0;
}

/*
A positive integer is of length n if and only if it has (n - 1) trailing zeros,
so the answer is the number of positive integers of length n that start or end with 1.

If the integer starts with 1, then the other (n - 1) digits can be any of the (n - 1) digits.
So there are n choices for the first digit, and for each of these, there are (n - 1) choices
for the other digits, giving a total of n * (n - 1) = 9 * (n - 1) integers.

If the integer ends with 1, then the first (n - 1) digits can be any of the 9 (n - 1) digits,
and there is 1 choice for the last digit, giving a total of 9 * (n - 1) integers.

Therefore, the total number of integers is 9 * (n - 1) + 1.

This is equivalent to the number of positive integers of length n that start or end with 1,
because if a number starts with 1, then it does not end with 1, and vice versa.
*/























































































































