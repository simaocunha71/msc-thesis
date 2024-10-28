    int i;
    int count=0;
    for (i=0;i<str.length();i++)
    {
        if (count<1)
        {
            count=0;
            while (i<str.length()&&str[i]==str[i-1])
            {
                count+=1;
                i+=1;
            }
        }
        else
        {
            count=0;
            while (i<str.length()&&str[i]!=str[i-1])
            {
                count+=1;
                i+=1;
            }
        }
    }
    return count;
}


