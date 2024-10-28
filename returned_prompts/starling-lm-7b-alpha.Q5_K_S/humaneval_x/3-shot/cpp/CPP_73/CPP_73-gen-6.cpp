    int i,j,left_index,right_index,change_count=0;
    int left_arr[arr.size()];
    int right_arr[arr.size()];
    int arr_size=arr.size();
    for (i=0;i<arr_size;i++)
    {
        left_arr[i]=arr[i];
        right_arr[i]=arr[arr_size-i-1];
    }
    for (i=0;i<arr_size;i++)
    {
        if (left_arr[i]!=right_arr[i])
        {
            change_count+=1;
        }
    }
    if (arr_size%2==1)
    {
        change_count-=1;
    }
    return change_count;
}



