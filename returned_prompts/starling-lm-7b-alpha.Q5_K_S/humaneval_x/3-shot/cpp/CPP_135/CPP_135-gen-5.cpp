    int i,prev_idx=-1;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]>arr[prev_idx])
        {
        prev_idx=i;
        }
    }
    if (prev_idx==-1)
    {
        return -1;
    }
    return prev_idx;
}


