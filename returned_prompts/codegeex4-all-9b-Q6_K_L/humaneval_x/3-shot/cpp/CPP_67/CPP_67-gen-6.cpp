    int apple,orange,mango;
    int i;
    int count=0;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a')
        {
            while (s[i+1]!=' ')
            {
                apple*=10;
                apple+=s[i+1]-48;
                i++;
            }
        }
        if (s[i]=='o')
        {
            while (s[i+1]!=' ')
            {
                orange*=10;
                orange+=s[i+1]-48;
                i++;
            }
        }
    }
    mango=n-apple-orange;
    return mango;
}

