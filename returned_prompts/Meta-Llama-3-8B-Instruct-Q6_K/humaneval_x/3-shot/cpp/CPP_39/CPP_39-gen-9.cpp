    int a=0,b=1,c;
    for (int i=1;i<n;i++)
    {
        c=a+b;
        if (c>1000000) break;
        a=b;
        b=c;
        if (is_prime(c))
        return c;
    }
    return 0;
}

bool is_prime(int n)
{
    if (n <= 1) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;

    for (int i = 3; i*i <= n; i += 2)
        if (n % i == 0)
            return false;

    return true;
}
// end of code
// end of code

Note: It seems like you are trying to solve some programming problems. If you are, please provide the problem statements as well, so that it's easier for others to understand the problem and provide better solutions. Also, please provide the expected output for each problem, if possible.