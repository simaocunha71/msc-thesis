    vector<int> res(n);
    for  (int i=1; i<=n; i++)
    {
        if  (i%2==0)
        {
            int fact=1;
            for  (int j=1; j<=i; j++)
            {
                fact=fact*j;
            }
            res[i-1]=fact;
        }
        else
        {
            int sum=0;
            for  (int j=1; j<=i; j++)
            {
                sum+=j;
            }
            res[i-1]=sum;
        }
    }
    return res;
}

