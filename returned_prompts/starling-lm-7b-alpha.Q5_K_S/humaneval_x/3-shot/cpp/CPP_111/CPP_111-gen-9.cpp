    map<char,int> result;
    char chr;
    int i,j;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (chr<='z' && chr>='a')
        {
            j=result.find(chr);
            if (j==result.end())
            {
                result[chr]=1;
            }
            else
            {
                result[chr]+=1;
            }
        }
    }
    return result;
}


