    int count_open_bracket=0;
    int count_close_bracket=0;
    int i;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
        count_open_bracket+=1;
        if (brackets[i]=='>')
        count_close_bracket+=1;
    }
    if (count_open_bracket==count_close_bracket)
    return true;
    return false;
}


