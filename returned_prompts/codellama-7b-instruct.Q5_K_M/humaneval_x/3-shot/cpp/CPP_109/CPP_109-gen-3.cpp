    int i,j;
    int temp;
    bool is_sorted=true;
    for (i=0;i<arr.size()-1;i++)
    {
        if (arr[i]>arr[i+1])
        is_sorted=false;
    }
    if (is_sorted)
    return true;
    
    for (i=0;i<arr.size()-1;i++)
    {
        if (arr[i]>arr[i+1])
        {
            temp=arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=temp;
            is_sorted=false;
        }
    }
    return move_one_ball(arr);
}



