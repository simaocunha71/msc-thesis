    int i,index=-1;
    for (i=0;i<arr.size();i++)
    {
        if (i==0)
        {
            index=i;
            continue;
        }
        if (arr[i]<arr[i-1])
        index=i;
    }
    return index;
}


