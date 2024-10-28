    int open_bracket=0;
    int i;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
        open_bracket+=1;
        if (brackets[i]=='>')
        open_brackets-=1;
        if (open_brackets<0)
        return false;
    }
    return (open_brackets==0);
}




