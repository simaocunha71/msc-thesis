    int i;
    int sum=0;
    int product=1;
    for (i=0;i<numbers.size();i++)
    {
        sum+=numbers[i];
        product*=numbers[i];
    }
    vector<int> ans;
    ans.push_back(sum);
    ans.push_back(product);
    return ans;
}

