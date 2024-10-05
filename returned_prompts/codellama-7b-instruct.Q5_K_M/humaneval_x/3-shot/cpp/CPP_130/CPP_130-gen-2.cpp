    vector<int> tribonacci;
    tribonacci.push_back(1);
    tribonacci.push_back(3);
    tribonacci.push_back(2);
    for (int i=4;i<=n;i++)
    {
        if (i%2==0)
        tribonacci.push_back(1+i/2);
        else
        tribonacci.push_back(tribonacci[i-2]+tribonacci[i-1]+tribonacci[i+1]);
    }
    return tribonacci;
}


