    int count_open_brackets=0;
    int count_close_brackets=0;
    int i;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
        count_open_brackets+=1;
        if (brackets[i]=='>')
        count_close_brackets+=1;
    }
    return count_open_brackets==count_close_brackets;
}


