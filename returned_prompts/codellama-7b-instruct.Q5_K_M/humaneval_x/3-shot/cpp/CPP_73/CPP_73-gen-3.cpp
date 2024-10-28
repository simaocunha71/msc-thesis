    int i,j;
    int min=INT_MAX;
    int temp;
    for (i=0;i<arr.size();i++)
    for (j=0;j<arr.size();j++)
    if (i!=j)
    if (abs(arr[i]-arr[j])<min)
    min=abs(arr[i]-arr[j]);
    return min;
}


