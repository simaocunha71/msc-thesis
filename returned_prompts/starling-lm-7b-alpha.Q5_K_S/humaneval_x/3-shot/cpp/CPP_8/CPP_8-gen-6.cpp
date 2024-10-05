    int i,sum=0;
    long long product=1;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    vector<int> result={sum,product};
    return result;
}


