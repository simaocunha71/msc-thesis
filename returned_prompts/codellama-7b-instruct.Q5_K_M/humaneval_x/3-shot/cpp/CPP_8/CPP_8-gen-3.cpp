    int sum=0;
    int product=1;
    for (int i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    vector<int> result;
    result.push_back(sum);
    result.push_back(product);
    return result;
}


