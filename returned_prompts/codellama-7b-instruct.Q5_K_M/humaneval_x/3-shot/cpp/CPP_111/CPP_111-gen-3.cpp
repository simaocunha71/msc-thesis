    map<char,int> hist;
    int i;
    char c;
    int max=0;
    for (i=0;i<test.length();i++)
    {
        c=test[i];
        if (hist.find(c)!=hist.end())
        hist[c]++;
        else
        hist[c]=1;

        if (hist[c]>max)
        max=hist[c];
    }
    return hist;
}



