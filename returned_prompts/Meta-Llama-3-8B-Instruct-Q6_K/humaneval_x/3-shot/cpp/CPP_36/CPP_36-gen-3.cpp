    int count=0;
    for (int i=1;i<n;i++)
    {
        if ((i%11==0) || (i%13==0))
        {
            char str[100];
            sprintf(str, "%d", i);
            for (int j=0;j<strlen(str);j++)
            {
                if (str[j]=='7')
                    count++;
            }
        }
    }
    return count;
}
