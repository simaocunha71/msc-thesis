    int max_count=0, max_num=-1;
    map<int,int> count_map;
    for (int i=0;i<lst.size();i++)
    {
        if (count_map.find(lst[i]) != count_map.end())
        {
            count_map[lst[i]]+=1;
        }
        else
        {
            count_map[lst[i]]=1;
        }
        if (count_map[lst[i]] > lst[i] && lst[i]>0)
        {
            max_count=count_map[lst[i]];
            max_num=lst[i];
        }
    }
    if (max_num<1)
        return -1;
    else
        return max_num;
}
