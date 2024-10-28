    int balance=0;
    char chr;
    for(int i=0;i<brackets.length();i++)
    {
        chr=brackets[i];
        if(chr=='(')
        balance++;
        else if(chr==')')
        balance--;
        if(balance<0)
        return false;
    }
    return balance==0;
}


