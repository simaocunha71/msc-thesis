    vector<int> tribonacci;
    int t1=1;
    int t2=3;
    int t3=2;
    int i;
    for (i=0;i<n+1;i++)
    {
        tribonacci.push_back(t1);
        if (i%2==0)
        {
            t1=t1+(n/2);
            continue;
        }
        t1=t2+t3+n;
        t2=t1-2;
        t3=t2-n;
    }
    return tribonacci;
}


