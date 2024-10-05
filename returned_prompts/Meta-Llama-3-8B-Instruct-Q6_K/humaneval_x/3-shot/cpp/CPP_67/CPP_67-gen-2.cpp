    int mango=0;
    int apples=0;
    int oranges=0;
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a')
        {
            if (s[i+1]=='p')
            {
                apples=0;
                i++;
                while (s[i]<'0' || s[i]>='9')
                i++;
                while (s[i]>='0'&&s[i]<='9')
                apples=apples*10+(s[i]-'0');
                i++;
                while (s[i]<'a' || s[i]>='z')
                i++;
            }
        }
        if (s[i]=='o')
        {
            if (s[i+1]=='r')
            {
                oranges=0;
                i++;
                while (s[i]<'0' || s[i]>='9')
                i++;
                while (s[i]>='0'&&s[i]<='9')
                oranges=oranges*10+(s[i]-'0');
                i++;
                while (s[i]<'o' || s[i]>='z')
                i++;
            }
        }
    }
    return n-apples-oranges;
}
