    int open=0,closed=0;
    int i;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
        open++;
        if (brackets[i]=='>')
        closed++;
        if (open<closed)
        return false;
    }
    if (open!=closed)
    return false;
    return true;
}