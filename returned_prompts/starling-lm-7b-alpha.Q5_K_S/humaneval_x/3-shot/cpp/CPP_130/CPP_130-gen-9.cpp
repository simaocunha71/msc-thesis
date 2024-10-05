    vector<int> result;
    int i,a,b,c;
    a=1; b=3; c=2;
    for (i=0;i<n+1;i++)
    {
        if (i%2==0)
        result.push_back(c);
        else
        result.push_back(a+b+c);
        int t=b; b=c; c=a+b+t; a=t;
    }
    return result;
}


