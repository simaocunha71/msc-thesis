    map<char,int> result;
    char chr;
    int i;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        result[chr]++;
    }
    return result;
}



