    vector<int> result;
    int i;
    int a,b,c;
    a=1;b=3;c=2;
    result.push_back(3);
    for (i=1;i<n+1;i++)
    {
        if (i%2==1)
        {
        c=(a+b+c)/2;
        a=b;b=c;
        }
        else
        {
        c=1+(i/2);
        }
        result.push_back(c);
    }
    return result;
}


