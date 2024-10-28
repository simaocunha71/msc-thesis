    if (arr.size()==0)
    return true;
    int i;
    for (i=0;i<arr.size();i++)
    {
        if (arr[i]>arr[i+1])
        return false;
    }
    return true;
}



