    int i;
    int min=arr[0];
    int min_index=0;
    for (i=1;i<arr.size();i++)
    {
        if (arr[i]%2==0 && arr[i]<min)
        {
            min=arr[i];
            min_index=i;
        }
    }
    if (min==arr[0] && min%2!=0)
    return {};
    return {min, min_index};
}

