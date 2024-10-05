    int smallest_even=-1;
    int smallest_index=-1;
    for (int i=0;i<arr.size();i++)
    {
        if (arr[i]%2==0)
        {
            if (smallest_even==-1)
            smallest_even=arr[i];
            if (smallest_even>arr[i])
            {
                smallest_even=arr[i];
                smallest_index=i;
            }
            if (smallest_even==arr[i] && smallest_index>i)
            smallest_index=i;
        }
    }
    if (smallest_even==-1)
    return {};
    return {smallest_even, smallest_index};
}


