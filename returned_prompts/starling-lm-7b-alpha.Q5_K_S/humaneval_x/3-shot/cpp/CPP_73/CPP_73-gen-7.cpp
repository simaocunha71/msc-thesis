    int i,j,count=0;
    int size=arr.size();
    for (i=0;i<size/2;i++)
    if (arr[i]!=arr[size-1-i])
    {
        count+=1;
    }
    if (size%2==1)
    if (arr[size/2]!=arr[size/2])
    count+=1;
    return count;
}



