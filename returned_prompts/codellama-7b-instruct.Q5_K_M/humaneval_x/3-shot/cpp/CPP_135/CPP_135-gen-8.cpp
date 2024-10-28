    int i,j;
    int max=-1;
    for (i=0;i<arr.size()-1;i++)
    for (j=i+1;j<arr.size();j++)
    if (arr[i]>=arr[j])
    max=i;
    return max;
}


