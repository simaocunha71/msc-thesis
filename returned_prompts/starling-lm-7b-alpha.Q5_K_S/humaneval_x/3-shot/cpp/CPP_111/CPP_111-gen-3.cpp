    map<char,int> result;
    char chr;
    int i,count;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        count=0;
        for (char c:test)
        {
            if (c==chr)
            count+=1;
        }
        result[chr]=count;
    }
    return result;
}




