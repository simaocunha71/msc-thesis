    int level=0;
    for (int i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        {
            level+=1;
        }
        if (str[i]==']')
        {
            level-=1;
        }
        if (level==0)
        {
            if (str[i+1]=='[')
                return true;
        }
    }
    return false;
}

