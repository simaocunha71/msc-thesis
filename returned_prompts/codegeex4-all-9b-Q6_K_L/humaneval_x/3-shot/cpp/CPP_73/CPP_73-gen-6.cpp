    int i;
    int changes=0;
    int arr_size=arr.size();
    for (i=0;i<arr_size/2;i++)
    if (arr[i]!=arr[arr_size-1-i])
    changes+=1;
    return changes;
}

