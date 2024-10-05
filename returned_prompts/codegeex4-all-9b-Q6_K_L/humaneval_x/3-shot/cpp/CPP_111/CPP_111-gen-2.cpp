    map<char,int> hist;
    for (int i=0;i<test.length();i++)
    {
        if (hist.find(test[i])==hist.end())
        hist[test[i]]=1;
        else
        hist[test[i]]+=1;
    }
    return hist;
}

