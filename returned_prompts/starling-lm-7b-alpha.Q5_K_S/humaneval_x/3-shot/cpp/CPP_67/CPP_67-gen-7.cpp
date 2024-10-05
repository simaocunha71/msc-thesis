    int i,count_apples=0,count_oranges=0;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr=='a')
        {
            count_apples+=1;
        }
        if (chr=='o')
        {
            count_oranges+=1;
        }
    }
    return n-count_apples-count_oranges;
}



