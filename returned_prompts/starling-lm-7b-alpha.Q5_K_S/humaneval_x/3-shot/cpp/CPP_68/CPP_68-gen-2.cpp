    int i,min_val=100000000;
    vector<int> result;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0 && arr[i]<min_val)
    {
        min_val=arr[i];
        result.clear();
        result.push_back(i);
    }
    else if (arr[i]%2==0 && arr[i]==min_val)
    result.push_back(i);

    return result;
}


