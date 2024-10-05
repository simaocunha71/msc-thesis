    int i,j;
    int odd_count=0;
    int total_odd_count=0;
    int change_count=0;
    for (i=0;i<arr.size();i++)
    {
        odd_count=0;
        for (j=0;j<arr.size();j++)
        {
            if (i==j) continue;
            if (arr[i]!=arr[j])
            {
                odd_count+=1;
            }
        }
        if (odd_count%2==1)
        {
        total_odd_count+=1;
        }
    }
    if (total_odd_count==0) return 0;
    if (total_odd_count%2==0) change_count=total_odd_count/2;
    if (total_odd_count%2==1) change_count=total_odd_count/2+1;
    return change_count;
}



