    int n = arr.size(), i, j;
    if(n==0)
        return true;
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < i; j++)
        {
            if(arr[j] > arr[i])
                break;
        }
        if(j == i)
            return true;
    }
    return false;
}


