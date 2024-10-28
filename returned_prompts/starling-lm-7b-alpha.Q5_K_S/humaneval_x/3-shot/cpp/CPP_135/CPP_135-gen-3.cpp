    int i,max_index;
    max_index=-1;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]>arr[max_index]||max_index==-1)
        max_index=i;
    }
    return max_index;
}




