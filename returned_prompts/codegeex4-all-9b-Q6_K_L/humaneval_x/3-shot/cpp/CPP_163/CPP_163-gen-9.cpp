    vector<int> all_ints;
    if (a>b)
    {
    int temp=a;
    a=b;
    b=temp;
    }
    for (int i=a;i<=b;i++)
    {
        int temp=i;
        while (temp>0)
        {
            int digit=temp%10;
            if (digit%2==0)
            {
            all_ints.push_back(digit);
            }
            temp=temp/10;
        }
    }
    return all_ints;
}

