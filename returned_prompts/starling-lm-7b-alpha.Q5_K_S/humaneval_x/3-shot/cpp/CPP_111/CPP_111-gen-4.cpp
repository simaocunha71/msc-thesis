    map<char,int> char_counts;
    int i,count;
    char chr;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (char_counts.find(chr)==char_counts.end())
        {
            count=1;
            char_counts[chr]=count;
        }
        else
        {
            count=char_counts[chr];
            count+=1;
            char_counts[chr]=count;
        }
    }
    return char_counts;
}

