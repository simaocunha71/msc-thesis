    int i,j;
    int count=0;
    int size=arr.size();
    int mid_index=size/2;
    for (i=0;i<mid_index;i++)
    {
        if (arr[i]!=arr[size-1-i])
        {
        count+=1;
        }
    }
    return count;
}



