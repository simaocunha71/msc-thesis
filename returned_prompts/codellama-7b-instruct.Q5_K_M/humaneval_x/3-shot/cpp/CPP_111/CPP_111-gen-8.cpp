    map<char,int> letter_count;
    char chr;
    int i;
    for (i=0;i<test.length();i++)
    {
        chr=test[i];
        if (isalpha(chr))
        letter_count[chr]++;
    }
    return letter_count;
}



