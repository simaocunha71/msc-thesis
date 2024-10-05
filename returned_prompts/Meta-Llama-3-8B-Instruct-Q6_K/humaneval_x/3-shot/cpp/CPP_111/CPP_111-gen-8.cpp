    map<char,int> histogram;
    string word;
    int max_count=0;
    int count;
    for (int i=0;i<test.length();i++)
    {
        if (test[i]==' ')
        {
            count=0;
            for (int j=i-1;j>=0;j--)
            {
                if (test[j]==' ')
                break;
                count++;
            }
            if (!histogram.count(word[0]))
            {
                histogram[word[0]]=count;
                if (count>max_count)
                max_count=count;
            }
            word="";
        }
        else
        word+=test[i];
    }
    count=0;
    for (int i=0;i<word.length();i++)
    {
        count++;
        if (!histogram.count(word[i]))
        {
            histogram[word[i]]=count;
            if (count>max_count)
            max_count=count;
        }
    }
    if (max_count>0)
    for (map<char,int>::iterator it=histogram.begin();it!=histogram.end();it++)
    {
        if (it->second==max_count)
        {
            histogram.insert(pair<char,int>(it->first,it->second));
        }
    }
    return histogram;
}