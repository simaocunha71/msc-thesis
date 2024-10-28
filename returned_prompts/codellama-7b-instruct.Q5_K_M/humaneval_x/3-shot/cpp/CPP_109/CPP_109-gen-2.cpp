    int i,j,k;
    for (i=0;i<arr.size();i++)
    for (j=i+1;j<arr.size();j++)
    if (arr[i]>arr[j])
    return false;
    return true;
}


