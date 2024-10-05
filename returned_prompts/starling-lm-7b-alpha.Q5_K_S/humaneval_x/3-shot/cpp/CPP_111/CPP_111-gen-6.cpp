    int i;
    int count=0;
    char chr;
    map<char,int> all_chars;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (all_chars.find(chr)==all_chars.end())
        {
        all_chars[chr]=1;
        }
        else
        {
        all_chars[chr]+=1;
        }
    }
    return all_chars;
}




