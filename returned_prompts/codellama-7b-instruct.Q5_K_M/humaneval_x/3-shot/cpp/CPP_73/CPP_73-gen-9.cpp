    int i,j;
    int min_changes=0;
    int changes=0;
    for (i=0;i<arr.size();i++)
    for (j=i+1;j<arr.size();j++)
    if (arr[i]!=arr[j])
    {
        changes++;
        if (abs(arr[i]-arr[j])==1)
        min_changes=min(changes,min_changes);
    }
    return min_changes;
}


