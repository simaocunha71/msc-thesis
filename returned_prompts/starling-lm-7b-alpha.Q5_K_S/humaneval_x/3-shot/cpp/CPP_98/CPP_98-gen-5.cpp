    int i;
    int count=0;
    int length=s.length();
    char chr;
    for (i=0;i<length;i++)
    {
        chr=s[i];
        if (i%2==0)
        {
            if (chr=='A' || chr=='E' || chr=='I' || chr=='O' || chr=='U')
            {
                count+=1;
            }
        }
    }
    return count;
}


