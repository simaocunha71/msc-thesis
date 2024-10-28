    int min_val = 10001, min_idx = -1;
    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] % 2 == 0 && arr[i] <= min_val)
        {
            min_val = arr[i];
            min_idx = i;
        }
    }
    if(min_idx != -1)
        return {min_val, min_idx};
    else
        return {};
}


