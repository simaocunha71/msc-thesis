    map<char,int> hist_map;
    char chr;
    int i;
    int count;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        count=hist_map[chr];
        hist_map[chr]=count+1;
    }

    return hist_map;
}

