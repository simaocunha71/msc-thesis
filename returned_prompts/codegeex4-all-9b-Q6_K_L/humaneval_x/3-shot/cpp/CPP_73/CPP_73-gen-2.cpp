    int i,j;
    int count=0;
    for (i=0;i<arr.size()/2;i++)
    for (j=arr.size()-1-i;j>=arr.size()/2;j--)
    if (arr[i]!=arr[j])
    count+=1;
    return count;
}

