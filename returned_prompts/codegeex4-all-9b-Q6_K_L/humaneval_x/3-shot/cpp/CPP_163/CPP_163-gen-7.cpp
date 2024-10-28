    vector<int> all_ints;
    int i;
    if (a>b)
    {
        i=a;
        a=b;
        b=i;
    }
    for (i=a;i<=b;i++)
    {
        int digit;
        while (i>0)
        {
            digit=i%10;
            if (digit%2==0)
            all_ints.push_back(digit);
            i/=10;
        }
    }
    return all_ints;
}

