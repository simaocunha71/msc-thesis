    int i,j;
    int count=0;
    int size=arr.size();
    for (i=0,j=size-1;i<j;i++,j--)
    {
        if (arr[i]!=arr[j])
        {
            count+=1;
        }
    }
    return count;
}

