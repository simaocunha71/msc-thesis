    map<char,int> result;
    int max_count=0;
    char max_letter=' ';
    for (int i=0;i<test.length();i++)
    {
        char chr=test[i];
        if (result.find(chr)==result.end())
            result[chr]=1;
        else
            result[chr]++;
        if (result[chr]>max_count)
        {
            max_count=result[chr];
            max_letter=chr;
        }
    }
    for (auto it=result.begin();it!=result.end();++it)
    {
        if (it->second==max_count)
            result[max_letter]=max_count;
        else
            result.erase(it->first);
    }
    return result;
} // end of function histogram



