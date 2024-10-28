    int min_changes=0;
    int i;
    for (i=0;i<arr.size();i++)
    if (arr[i]!=arr[arr.size()-1-i])
    min_changes++;
    return min_changes;
}


