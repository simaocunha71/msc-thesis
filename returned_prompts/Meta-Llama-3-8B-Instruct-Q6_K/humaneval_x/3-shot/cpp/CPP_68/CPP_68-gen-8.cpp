    int smallest_value=INT_MAX;
    int smallest_index=-1;
    for(int i=0;i<arr.size();i++)
    {
        if(arr[i]%2==0 && arr[i]<smallest_value)
        {
            smallest_value=arr[i];
            smallest_index=i;
        }
    }
    if(smallest_value==INT_MAX)
        return {};
    else
        return {smallest_value, smallest_index};
}
