    int i;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        {
            if (str[i+1]==']')
            return true;
        }
    }
    return false;
}


