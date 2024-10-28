    int counter=0;
    char chr;
    int i;
    for  (i=0;i<brackets.length();i++)
    {
        chr=brackets[i];
        if  (chr=='(')
            counter+=1;
        if  (chr==')')
            counter-=1;
        if (counter<0)
            return false;
    }
    return (counter==0);
}



