    int i;
    int index;
    int smallest_value;
    bool found=false;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]%2==0)
        {
            found=true;
            if (smallest_value==0 || arr[i]<smallest_value)
            {
                smallest_value=arr[i];
                index=i;
            }
        }
    }
    if (found)
    {
        return {smallest_value, index};
    }
    else
    {
        return {};
    }
}


