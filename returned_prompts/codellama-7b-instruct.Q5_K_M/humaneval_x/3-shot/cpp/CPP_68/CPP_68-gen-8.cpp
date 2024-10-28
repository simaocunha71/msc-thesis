    int i,j,min=10000,min_index=0;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0)
    if (arr[i]<min)
    {
        min=arr[i];
        min_index=i;
    }
    vector<int> result;
    if (min!=10000)
    {
    result.push_back(min);
    result.push_back(min_index);
    }
    return result;
}


