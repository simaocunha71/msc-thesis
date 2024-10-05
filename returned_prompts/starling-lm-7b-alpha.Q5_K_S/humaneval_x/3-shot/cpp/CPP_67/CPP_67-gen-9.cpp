    int i,count=0,total=0;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr=='a')
        {
            count+=1;
        }
        if (chr=='o')
        {
            count+=1;
        }
        if (chr=='m')
        {
            total+=1;
        }
    }
    return n-count-total;
}


