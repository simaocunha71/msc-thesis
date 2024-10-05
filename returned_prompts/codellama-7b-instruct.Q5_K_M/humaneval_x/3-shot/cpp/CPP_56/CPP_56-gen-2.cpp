    int i;
    int counter=0;
    for (i=0;i<brackets.length();i++)
    if (brackets[i]=='<')
    counter+=1;
    for (i=0;i<brackets.length();i++)
    if (brackets[i]=='>')
    counter-=1;
    if (counter==0)
    return true;
    else
    return false;
}


