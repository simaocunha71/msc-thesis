    map<char,int> histogram;
    int i,j;
    for (i=0;i<test.length();i++)
    {
        char chr=test[i];
        histogram[chr]+=1;
    }
    return histogram;
}


