    vector<int> all;
    int i;

    if (a>b)
    {
        int c;
        c=a;
        a=b;
        b=c;
    }

    for (i=a;i<=b;i++)
    if (i%2==0)
    all.push_back(i);
    return all;
}

