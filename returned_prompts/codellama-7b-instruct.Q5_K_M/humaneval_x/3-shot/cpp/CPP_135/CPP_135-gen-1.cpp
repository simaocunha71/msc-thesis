    int i;
    int max_index=-1;
    int prev_num=-1;
    int num;
    for (i=0;i<arr.size();i++)
    {
        num=arr[i];
        if (num<prev_num)
        max_index=i-1;
        if (num>prev_num)
        max_index=i;
        prev_num=num;
    }
    return max_index;
}


