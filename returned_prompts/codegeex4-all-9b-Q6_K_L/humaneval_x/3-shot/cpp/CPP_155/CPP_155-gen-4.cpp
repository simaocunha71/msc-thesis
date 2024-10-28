    int count_even=0,count_odd=0;
    int n;
    if (num<0) n=-num;
    else n=num;
    while (n>0)
    {
        if (n%2==0) count_even+=1;
        else count_odd+=1;
        n=n/10;
    }
    return {count_even,count_odd};
}

