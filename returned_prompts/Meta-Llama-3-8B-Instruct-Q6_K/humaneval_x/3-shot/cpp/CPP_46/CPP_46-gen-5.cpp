    if (n<=3) return 0;
    int a=0, b=0, c=2, d=0;
    for (int i=4;i<=n;i++)
    {
        int sum=a+b+c;
        a=b;
        b=c;
        c=d;
        d=sum;
    }
    return d;
}  // time complexity O(n)  // space complexity O(1)  // This function uses a loop to compute the nth element of the fib4 sequence. It uses four variables to keep track of the last four elements of the sequence, and then updates these variables in each iteration of the loop. This way it avoids the need for recursion and reduces the time complexity to O(n). The space complexity is O(1) because it only uses a constant amount of space.