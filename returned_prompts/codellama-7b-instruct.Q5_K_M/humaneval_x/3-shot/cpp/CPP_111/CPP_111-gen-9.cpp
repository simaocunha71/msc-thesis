    map<char,int> hist;
    int len=test.length();
    int i;
    char current;
    for (i=0;i<len;i++)
    {
        current=test[i];
        hist[current]++;
    }
    return hist;
}


