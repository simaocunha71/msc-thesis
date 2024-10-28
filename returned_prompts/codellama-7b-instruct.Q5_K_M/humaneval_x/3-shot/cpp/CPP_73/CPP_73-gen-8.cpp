    int i,j;
    int min=999999999;
    for (i=0;i<arr.size();i++)
    for (j=0;j<arr.size();j++)
    if (abs(arr[i]-arr[j])<min && i!=j){
        min=abs(arr[i]-arr[j]);
    }
    return min;
}

