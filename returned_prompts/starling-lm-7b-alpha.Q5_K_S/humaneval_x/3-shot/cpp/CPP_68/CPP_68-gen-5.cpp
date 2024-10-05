    int i;
    int value=INT_MAX;
    int index=-1;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0 && arr[i]<value)
    {
        value=arr[i];
        index=i;
    }

    if (index!=-1)
    return {value,index};
    else
    return {};
}





