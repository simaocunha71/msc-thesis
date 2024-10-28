    int i,j;
    for (i=0;i<arr.size();i++)
    {
        for (j=i+1;j<arr.size();j++)
        {
            if (bin_count(arr[i])>bin_count(arr[j]))
            swap(arr[i],arr[j]);
            else if (bin_count(arr[i])==bin_count(arr[j]))
            if (arr[i]>arr[j])
            swap(arr[i],arr[j]);
        }
    }
    return arr;
}


