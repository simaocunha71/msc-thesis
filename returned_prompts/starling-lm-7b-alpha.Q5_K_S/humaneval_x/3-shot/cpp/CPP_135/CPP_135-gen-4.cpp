    int i,max;
    if (arr.size()==1)
    return 0;
    max=arr[0];
    for (i=1;i<arr.size();i++)
    if (arr[i]>max)
    {
        max=arr[i];
        while (i+1<arr.size() && arr[i+1]>max)
        i+=1;
        return i;
    }
    return -1;
}



