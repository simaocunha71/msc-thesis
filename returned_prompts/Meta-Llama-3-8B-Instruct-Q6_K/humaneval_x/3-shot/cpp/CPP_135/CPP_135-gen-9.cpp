    int i;
    for (i=1;i<arr.size();i++)
    if (arr[i-1]>arr[i])
    return i-1;
    return -1;
} 



