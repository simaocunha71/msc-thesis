    int i,fib_num,curr_fib=0,prev_fib=1,sum_fib;
    for (i=3;i<=n;i++)
    {
        fib_num=curr_fib+prev_fib;
        if (fib_num%2!=0 && fib_num%3!=0 && fib_num%5!=0 && fib_num%7!=0)
        {
            return fib_num;
        }
        curr_fib=prev_fib;
        prev_fib=fib_num;
    }
    return -1;
}


