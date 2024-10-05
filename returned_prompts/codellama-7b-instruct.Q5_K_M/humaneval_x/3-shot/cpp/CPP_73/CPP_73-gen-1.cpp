    int i,j;
    int min_changes=0;
    int tmp;
    for (i=0;i<arr.size();i++)
    for (j=0;j<arr.size();j++)
    if (arr[i]==arr[j]){
        tmp=abs(i-j);
        if (tmp>min_changes)
        min_changes=tmp;
    }
    return min_changes;
}



