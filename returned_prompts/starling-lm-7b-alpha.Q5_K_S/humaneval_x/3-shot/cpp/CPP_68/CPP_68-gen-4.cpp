    int i,n;
    vector<int> res;
    n=arr.size();
    int smallest_even=-1;
    int index=-1;
    for (i=0;i<n;i++)
    if (arr[i]%2==0 && smallest_even==-1)
    {
        smallest_even=arr[i];
        index=i;
    }
    else if (arr[i]%2==0 && smallest_even!=arr[i])
    {
        smallest_even=arr[i];
        index=i;
    }
    res.push_back(smallest_even);
    res.push_back(index);
    return res;
}




