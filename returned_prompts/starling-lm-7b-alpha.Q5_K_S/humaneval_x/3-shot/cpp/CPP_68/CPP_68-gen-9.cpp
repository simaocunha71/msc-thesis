    int i,min_index;
    vector<int> min_values;
    int smallest_even=INT_MAX;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0 && arr[i]<smallest_even)
    {
        smallest_even=arr[i];
        min_index=i;
        min_values.clear();
    }
    if (min_values.size()==0)
    return {};
    else if (min_values.size()==1)
    return {min_values[0],min_index};
    else
    return {min_values[0],min_index};
}

