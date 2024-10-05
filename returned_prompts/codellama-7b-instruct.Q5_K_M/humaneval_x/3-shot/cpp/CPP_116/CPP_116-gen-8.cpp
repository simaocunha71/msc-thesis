    vector<pair<int,int>> v;
    for (int i=0;i<arr.size();i++)
    {
        int num=arr[i];
        int num_ones=0;
        while (num)
        {
            num_ones+=num%2;
            num=num/2;
        }
        v.push_back({num_ones, arr[i]});
    }
    sort(v.begin(), v.end());
    for (int i=0;i<v.size();i++)
    arr[i]=v[i].second;
    return arr;
}


