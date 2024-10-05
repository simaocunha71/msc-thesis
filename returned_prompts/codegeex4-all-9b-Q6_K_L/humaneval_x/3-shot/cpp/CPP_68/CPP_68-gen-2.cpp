    int i;
    int min=1000000;
    int min_index;
    int value;
    for (i=0;i<arr.size();i++)
    {
        value=arr[i];
        if (value%2==0)
        {
            if (value<min)
            {
                min=value;
                min_index=i;
            }
        }
    }
    if (min!=1000000)
    return {min,min_index};
    else
    return {};
}