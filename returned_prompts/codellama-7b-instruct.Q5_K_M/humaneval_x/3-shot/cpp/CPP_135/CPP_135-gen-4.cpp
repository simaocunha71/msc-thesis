    int i,j;
    int largest_index=-1;
    int current_largest_index;
    int largest_value;
    for (i=arr.size()-1;i>=0;i--)
    {
    largest_value=arr[i];
    for (j=i-1;j>=0;j--)
    if (arr[j]>largest_value)
    {
        largest_index=j;
        break;
    }
    if (largest_index==-1)
    return i;
    else
    largest_index=-1;
    }
    return -1;
}



