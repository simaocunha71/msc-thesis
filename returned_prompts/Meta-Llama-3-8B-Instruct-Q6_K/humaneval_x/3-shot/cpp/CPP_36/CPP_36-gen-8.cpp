    int count=0;
    int i;
    for (i=11;i<n;i++)
    {
        if ((i%11==0)||(i%13==0))
        {
            char chr[10];
            itoa(i,chr,10);
            for (int j=0;j<strlen(chr);j++)
            {
                if (chr[j]=='7')
                count++;
            }
        }
    }
    for (i=13;i<n;i++)
    {
        if (i%13==0)
        {
            char chr[10];
            itoa(i,chr,10);
            for (int j=0;j<strlen(chr);j++)
            {
                if (chr[j]=='7')
                count++;
            }
        }
    }
    return count;
} 



