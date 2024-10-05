    map<char,int> histogram;
    for (int i=0;i<test.length();i++)
    {
        char c=test[i];
        if (histogram.find(c)!=histogram.end())
        {
            histogram[c]++;
        }
        else
        {
            histogram[c]=1;
        }
    }
    map<char,int> max_map;
    int max_value=0;
    for (auto it=histogram.begin();it!=histogram.end();it++)
    {
        if (it->second > max_value)
        {
            max_value=it->second;
            max_map=map<char,int>();
            max_map[it->first]=it->second;
        }
        else if (it->second == max_value)
        {
            max_map[it->first]=it->second;
        }
    }
    return max_map;
}