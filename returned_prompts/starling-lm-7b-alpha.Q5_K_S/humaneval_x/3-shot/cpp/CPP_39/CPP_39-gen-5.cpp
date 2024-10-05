    int fib,i;
    int fib_numbers[]={0,1};
    for (i=2;i<=n;i++)
    {
        fib=fib_numbers[fib_numbers.size()-1]+fib_numbers[fib_numbers.size()-2];
        fib_numbers.push_back(fib);
        if (fib>3 && fib%2!=0 && fib%3!=0 && fib%5!=0 && fib%7!=0)
        {
            return fib;
        }
    }
    return -1;
}



