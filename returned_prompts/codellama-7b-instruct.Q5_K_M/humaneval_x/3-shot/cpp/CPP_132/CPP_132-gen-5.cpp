    int count_open = 0;
    int count_close = 0;
    for (int i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        count_open+=1;
        if (str[i]==']')
        count_close+=1;
    }
    if (count_open==count_close)
    return false;
    else
    return true;
}



