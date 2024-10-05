    int open_brackets=0;
    int i;
    for (i=0;i<brackets.length();i++)
    if (brackets[i]=='<')
    open_brackets+=1;
    for (i=0;i<brackets.length();i++)
    if (brackets[i]=='>')
    open_brackets-=1;
    if (open_brackets==0)
    return true;
    else
    return false;
}


