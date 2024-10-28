    int i;
    int small_change=0;
    int size=arr.size();
    vector<int> temp_arr;
    for (i=0;i<size;i++)
    temp_arr.push_back(arr[i]);
    for (i=0;i<size;i++)
    {
        if (temp_arr[i]!=arr[i])
        small_change+=1;
        if (temp_arr[size-i-1]!=arr[i])
        small_change+=1;
    }
    return small_change;
}


