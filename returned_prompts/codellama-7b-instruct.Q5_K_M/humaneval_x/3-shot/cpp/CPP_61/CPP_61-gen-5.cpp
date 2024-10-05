    int level=0;
    char chr;
    int i;
    for (i=0;i<brackets.length();i++){
        chr=brackets[i];
        if (chr=='(')
        level+=1;
        if (chr==')')
        level-=1;
        if (level<0)
        return false;
    }
    return level==0;
}


