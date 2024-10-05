    int i;
    int open_brackets=0;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='(')
        open_brackets+=1;
        if (brackets[i]==')')
        open_brackets-=1;
    }
    if (open_brackets==0)
    return true;
    else
    return false;
}


