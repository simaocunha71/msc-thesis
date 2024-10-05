    int i=0;
    for (i=0;i<str.length();i++)
    if (str[i]=='[')
    {
        if (str[i+1]==']')
        return false;
        else
        return true;
    }
    return false;
}

