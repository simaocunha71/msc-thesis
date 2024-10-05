    int smallest = 999999999;
    int smallest_index = -1;
    int i;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]%2==0 && arr[i]<smallest)
        {
            smallest=arr[i];
            smallest_index=i;
        }
    }
    vector<int> v;
    if (smallest_index!=-1)
    {
        v.push_back(smallest);
        v.push_back(smallest_index);
    }
    return v;
}



