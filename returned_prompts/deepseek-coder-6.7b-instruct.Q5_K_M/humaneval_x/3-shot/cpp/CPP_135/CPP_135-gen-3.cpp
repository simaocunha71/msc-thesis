    for(int i=arr.size()-1;i>0;i--)
    {
        if(arr[i]<arr[i-1])
        return i;
    }
    return -1;
}


