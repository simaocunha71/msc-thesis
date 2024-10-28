    int i,j;
    int open_brackets=0;
    char chr;
    bool result=true;
    for (i=0;i<brackets.length();i++)
    {
        chr=brackets[i];
        if (chr=='<')
            open_brackets+=1;
        if (chr=='>')
            open_brackets-=1;

        if (open_brackets<0)
            result=false;
    }
    if (open_brackets!=0)
        result=false;

    return result;
}


