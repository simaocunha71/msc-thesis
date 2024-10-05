    int count=0;
    for(int i=11;i<n;i++)
    {
        if(i%11==0 || i%13==0)
        {
            char str[10];
            itoa(i,str,10);
            for(int j=0;j<strlen(str);j++)
            {
                if(str[j]=='7')
                count++;
            }
        }
    }
    for(int i=13;i<n;i++)
    {
        if(i%11==0 || i%13==0)
        {
            char str[10];
            itoa(i,str,10);
            for(int j=0;j<strlen(str);j++)
            {
                if(str[j]=='7')
                count++;
            }
        }
    }
    return count;
}