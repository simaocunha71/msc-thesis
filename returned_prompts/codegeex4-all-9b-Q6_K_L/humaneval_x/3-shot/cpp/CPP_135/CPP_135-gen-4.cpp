    int i;
    int size=arr.size();
    for (i=1;i<size;i++)
    {
        if (arr[i]<arr[i-1])
        return i-1;
    }
    return -1;
}

