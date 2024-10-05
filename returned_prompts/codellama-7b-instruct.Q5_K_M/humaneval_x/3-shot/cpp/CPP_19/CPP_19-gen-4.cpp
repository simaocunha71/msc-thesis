    map<string, int> num_map;
    string num;
    string sorted_nums;
    int i;
    int j;
    for (i=0;i<numbers.length();i++)
    {
        num=numbers[i];
        if (num_map.count(num)==0)
        num_map[num]=1;
        else
        num_map[num]+=1;
    }
    for (auto it=num_map.begin();it!=num_map.end();it++)
    {
        num=it->first;
        j=it->second;
        while (j-->0)
        sorted_nums+=num;
    }
    return sorted_nums;
}


