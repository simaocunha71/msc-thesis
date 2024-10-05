    map<char,int> histogram;
    int i;
    int max_count=0;
    char max_char;
    for (i=0;i<test.length();i++)
    {
        char chr=test[i];
        if (histogram.find(chr)!=histogram.end())
        histogram[chr]++;
        else
        histogram[chr]=1;
        if (histogram[chr]>max_count)
        {
            max_count=histogram[chr];
            max_char=chr;
        }
    }
    map<char,int> result;
    for (i=0;i<histogram.size();i++)
    {
        if (histogram[i]->second==max_count)
        result[i]=max_count;
    }
    return result;
}