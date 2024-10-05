    map<char,int> letters;
    char chr;
    int i;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (chr==' ') continue;
        if (letters.find(chr)!=letters.end())
        {
        letters[chr]+=1;
        }
        else
        {
        letters[chr]=1;
        }
    }
    return letters;
}



