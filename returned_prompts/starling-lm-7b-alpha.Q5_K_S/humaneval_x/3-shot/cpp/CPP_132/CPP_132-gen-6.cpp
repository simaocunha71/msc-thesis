    int i;
    int square_brackets=0;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        square_brackets+=1;
        if (str[i]==']')
        square_brackets-=1;
        if (square_brackets<0)
        return true;
    }
    return false;
}



