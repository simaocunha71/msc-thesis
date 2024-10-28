    int i,max_index=-1;
    for (i=0;i<arr.size();i++)
    {
        if (i<max_index && arr[i]>arr[i-1])
        {
            return max_index;
        }
        if (i>max_index && arr[i]<=arr[i-1])
        {
            max_index=i;
        }
    }
    return max_index;
}



