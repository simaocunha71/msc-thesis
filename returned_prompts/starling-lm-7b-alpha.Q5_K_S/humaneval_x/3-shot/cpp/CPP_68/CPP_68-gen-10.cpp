    int i;
    int even_val=-1;
    int even_index=-1;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0 && (even_val==-1 || arr[i]<even_val || (arr[i]==even_val && even_index>i)))
    {
        even_val=arr[i];
        even_index=i;
    }
    if (even_val==-1)
    return {};
    return {even_val,even_index};
}


