    int sum=0;
    int product=1;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    vector<int> result={sum,product};
    return result;
}


