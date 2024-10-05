    int i,j;
    int min=arr[0];
    int max=arr[0];
    int index_min=0;
    int index_max=0;
    for (i=0;i<arr.size();i++)
    {
    if (arr[i]>max)
    {
    max=arr[i];
    index_max=i;
    }
    if (arr[i]<min)
    {
    min=arr[i];
    index_min=i;
    }
    }
    if (index_min>index_max)
    return true;
    else
    return false;
}

