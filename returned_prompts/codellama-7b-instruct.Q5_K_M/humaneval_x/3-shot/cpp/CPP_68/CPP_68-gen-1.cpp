    vector<int> result;
    int smallest_even_value=10000, smallest_even_index=0;
    for (int i=0;i<arr.size();i++)
    {
        if (arr[i]%2==0 && arr[i]<smallest_even_value)
        {
            smallest_even_value=arr[i];
            smallest_even_index=i;
        }
    }
    if (smallest_even_value==10000)
    {
        return result;
    }
    result.push_back(smallest_even_value);
    result.push_back(smallest_even_index);
    return result;
}


