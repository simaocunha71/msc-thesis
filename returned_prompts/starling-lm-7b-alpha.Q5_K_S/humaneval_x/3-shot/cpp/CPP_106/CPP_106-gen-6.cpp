    vector<int> numbers;
    int i,factorial;
    for (i=1;i<=n;i++)
    {
        if (i%2==0){
            factorial=1;
            for (int j=1;j<=i;j++)
                factorial*=j;
            numbers.push_back(factorial);
        }
        if (i%2!=0)
        {
            int sum=0;
            for (int j=1;j<=i;j++)
                sum+=j;
            numbers.push_back(sum);
        }
    }
    return numbers;
}


