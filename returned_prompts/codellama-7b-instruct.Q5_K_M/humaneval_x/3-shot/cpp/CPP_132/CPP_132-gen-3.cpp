    int i,j;
    int open_bracket=0;
    int close_bracket=0;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        {
            open_bracket+=1;
        }
        if (str[i]==']')
        {
            close_bracket+=1;
        }
    }
    if ((open_bracket>close_bracket)&&(close_bracket!=0))
    return true;
    else
    return false;
}



