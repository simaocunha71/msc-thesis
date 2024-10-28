    int open_brackets=0;
    int i;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        open_brackets+=1;
        if (str[i]==']')
        open_brackets-=1;
        if (open_brackets<0)
        return false;
    }
    if (open_brackets!=0)
    return false;
    return true;
}


