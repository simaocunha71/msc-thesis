    int sum=0;
    int prod=1;
    for (int i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        prod*=numbers[i];
    }
    vector<int> res;
    res.push_back(sum);
    res.push_back(prod);
    return res;
}



