    int a=0,b=1,fib_num=1;
    int count=0;
    while (count<n)
    {
        int temp=a+b;
        a=b;
        b=temp;
        if (is_prime(temp))
        {
            fib_num=temp;
            count++;
        }
    }
    return fib_num;
}

bool is_prime(int num)
{
    if (num<2) return false;
    for (int i=2;i*i<=num;i++)
    if (num%i==0) return false;
    return true;
}  // This is a helper function to check if a number is prime
}  // End of namespace std.
#endif
