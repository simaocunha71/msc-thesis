    int sum=0;
    long long product=1;
    int i;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    vector<int> result;
    result.push_back(sum);
    result.push_back(product);
    return result;
}



