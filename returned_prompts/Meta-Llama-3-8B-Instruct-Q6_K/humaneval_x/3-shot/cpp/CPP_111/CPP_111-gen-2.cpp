    map<char,int> result;
    int max_count=0;
    for (int i=0;i<test.length();i++)
    {
        char c=test[i];
        if (result.find(c)!=result.end())
        {
            result[c]++;
        }
        else
        {
            result[c]=1;
        }
        if (result[c]>max_count)
        {
            max_count=result[c];
        }
    }
    map<char,int> max_map;
    for (auto it=result.begin();it!=result.end();it++)
    {
        if (it->second==max_count)
        {
            max_map[it->first]=it->second;
        }
    }
    return max_map;
}