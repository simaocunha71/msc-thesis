    int i,j;
    
    for (i=0;i<arr.size();i++)
    for (j=i+1;j<arr.size();j++)
    if (arr[j]>=arr[i])
    return i;

    return -1;
}

