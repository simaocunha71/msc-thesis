    map<char,int> result;
    int i,j;
    char chr;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (chr==' '){}
        else
        {
            if (result.find(chr)==result.end())
            result[chr]=1;
            else
            result[chr]+=1;
        }
    }
    return result;
}


