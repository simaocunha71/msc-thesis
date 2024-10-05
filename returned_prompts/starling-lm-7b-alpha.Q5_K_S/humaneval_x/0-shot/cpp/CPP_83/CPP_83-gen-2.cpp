    if(n==0)
        return 0;
    if(n==1)
        return 1;
    else
        return 2*starts_one_ends(n-1);
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d",starts_one_ends(n));
    return 0;
}












































/*
Given a positive integer n, return the count of the numbers of n-digit positive integers that start or end with 1.

Example:

For n = 3, the possible 3-digit numbers that start or end with 1 are: 100, 101, 110, 120, 130, ..., 199, 1000, 1001, 1010, 1011, 1100, 1101, 1200, ..., 1999.
So the total number of such 3-digit numbers is 18.

For n = 4, there are 36 such 4-digit numbers.
For n = 5, there are 64 such 5-digit numbers.

Here are the numbers of 4-digit and 5-digit numbers that start or end with 1.

4-digit numbers: 1000, 1001, 1010, 1011, 1100, 1101, ..., 1990, 1991
5-digit numbers: 10000, 10001, 10010, 10011, ..., 19990, 19991

We can see that there are 36 such 4-digit numbers and 64 such 5-digit numbers.

We can observe that there are 2