    int i,j;
    for (i=arr.size()-2;i>=0;i--)
    if (arr[i]<arr[i+1])
    return i;
    return -1;
}


