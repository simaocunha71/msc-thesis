    int i,j,k;
    int count=0;
    int max=INT_MIN;
    for (i=0;i<arr.size();i++)
    for (j=0;j<arr.size();j++)
    if (abs(arr[i]-arr[j])>max)
    max=abs(arr[i]-arr[j]);
    for (i=0;i<arr.size();i++)
    if (arr[i]!=arr[(arr.size()-1)-i])
    count++;
    return max+count;
}


