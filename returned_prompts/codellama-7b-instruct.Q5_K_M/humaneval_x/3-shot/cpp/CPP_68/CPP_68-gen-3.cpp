    int smallest_even_value=1000000000;
    int smallest_even_index=0;
    int i;
    for (i=0;i<arr.size();i++)
    if (arr[i]%2==0)
    if (smallest_even_value>arr[i])
    {
        smallest_even_value=arr[i];
        smallest_even_index=i;
    }
    if (smallest_even_index==0)
    return {smallest_even_value, smallest_even_index};
    if (smallest_even_index==arr.size()-1)
    return {smallest_even_value, smallest_even_index-1};
    if (smallest_even_index>0 && smallest_even_index<arr.size()-1)
    return {smallest_even_value, smallest_even_index-1};
}



