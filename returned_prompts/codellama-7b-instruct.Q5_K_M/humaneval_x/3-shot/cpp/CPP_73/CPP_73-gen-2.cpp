    int i,j,k;
    int min_changes=INT_MAX;
    for (i=0;i<arr.size();i++)
    for (j=i+1;j<arr.size();j++)
    for (k=j+1;k<arr.size();k++)
    if (abs(arr[i]-arr[j])<min_changes&&abs(arr[j]-arr[k])<min_changes){
        min_changes=abs(arr[i]-arr[j])+abs(arr[j]-arr[k]);
        if (min_changes==0)
        break;
    }
    return min_changes;
}



