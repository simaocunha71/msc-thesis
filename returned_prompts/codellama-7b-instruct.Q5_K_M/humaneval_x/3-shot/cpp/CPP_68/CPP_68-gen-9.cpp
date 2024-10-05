    int smallest_even_val=10000000;
    int smallest_even_index=0;
    int smallest_index=0;
    int i;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]%2==0)
        {
            if (arr[i]<smallest_even_val)
            {
                smallest_even_val=arr[i];
                smallest_even_index=i;
            }
            else if (arr[i]==smallest_even_val && i<smallest_index)
            smallest_even_index=i;
        }
        if (arr[i]<smallest_even_val)
            smallest_index=i;
        else if (arr[i]==smallest_even_val && i<smallest_index)
            smallest_index=i;
    }
    if (smallest_even_val==10000000)
    return {};
    return {smallest_even_val, smallest_even_index};
}



