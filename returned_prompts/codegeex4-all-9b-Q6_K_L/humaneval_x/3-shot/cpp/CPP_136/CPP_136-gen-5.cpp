    int i,large_num=0,small_num=0;
    for (i=0;i<lst.size();i++)
    {
        if (lst[i]<0)
        {
            if (lst[i]<large_num)
            large_num=lst[i];
        }
        if (lst[i]>0)
        {
            if (lst[i]>small_num)
            small_num=lst[i];
        }
    }
    vector<int> result={large_num,small_num};
    return result;
}

