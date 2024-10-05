    map<char,int> result;
    string::size_type i;
    for (i=0;i<test.length();i++)
    {
        char chr=test[i];
        if (result.find(chr)!=result.end())
        {
            result[chr]++;
        }
        else
        {
            result[chr]=1;
        }
    }
    map<char,int> max_map;
    int max_count=0;
    map<char,int>::iterator it;
    for (it=result.begin();it!=result.end();it++)
    {
        if (it->second>max_count)
        {
            max_count=it->second;
            max_map.clear();
            max_map[it->first]=max_count;
        }
        else if (it->second==max_count)
        {
            max_map[it->first]=max_count;
        }
    }
    return max_map;
} 



