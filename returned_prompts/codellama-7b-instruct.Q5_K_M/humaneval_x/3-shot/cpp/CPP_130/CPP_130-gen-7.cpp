    vector<int> tribonacci;
    if (n==0)
    return tribonacci;
    if (n==1)
    {
        tribonacci.push_back(1);
        return tribonacci;
    }
    if (n==2)
    {
        tribonacci.push_back(1);
        tribonacci.push_back(3);
        tribonacci.push_back(2);
        return tribonacci;
    }

    tribonacci.push_back(1);
    tribonacci.push_back(3);
    tribonacci.push_back(2);
    for (int i=3;i<n;i++)
    {
        if (i%2==0)
        {
            tribonacci.push_back(1+(i/2));
        }
        else
        {
            tribonacci.push_back(tribonacci[i-1]+tribonacci[i-2]+tribonacci[i+1]);
        }
    }
    tribonacci.push_back(tribonacci[n-1]+tribonacci[n-2]+tribonacci[n+1]);
    return tribonacci;
}


