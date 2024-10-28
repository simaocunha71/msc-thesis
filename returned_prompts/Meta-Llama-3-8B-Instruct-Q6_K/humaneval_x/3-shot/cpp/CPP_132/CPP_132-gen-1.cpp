    int level=0;
    for (int i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        level++;
        else if (str[i]==']')
        {
            level--;
            if (level<0)
            return true;
        }
    }
    return false;
}