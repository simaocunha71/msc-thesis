    if (arr.size()==0) return true;
    int i,j;
    for (i=0;i<arr.size();i++)
    for (j=i+1;j<arr.size();j++)
    if (arr[j]<arr[i])
    return false;
    return true;
}


