    vector<int> result;
    int i,min_value=INT_MAX;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]%2==0 && arr[i]<min_value)
        {
            min_value=arr[i];
            result[0]=i;
        }
    }
    if (result.size()==0)
    return {};
    return {min_value,result[0]};
}



