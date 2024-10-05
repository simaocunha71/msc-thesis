    int i,j;
    for (i=0;i<arr.size()-1;i++)
    {
        if (arr[i]>arr[i+1])
        return i;
    }
    return -1;
}

