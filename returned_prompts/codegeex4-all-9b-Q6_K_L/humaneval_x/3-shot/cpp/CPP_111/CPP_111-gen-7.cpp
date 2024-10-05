    map<char,int> histogram;
    string chr;
    int i;
    int count=0;
    int max=0;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        count=0;
        for (int j=0;j<test.length();j++)
        {
            if (chr==test[j])
            count+=1;
        }
        histogram.insert(pair<char,int>(chr,count));
        if (count>max)
        max=count;
    }
    map<char,int>::iterator it;
    for (it=histogram.begin();it!=histogram.end();it++)
    {
        if (it->second!=max)
        histogram.erase(it->first);
    }
    return histogram;
}

