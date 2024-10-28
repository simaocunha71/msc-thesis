    int count=0;
    int i;
    for (i=0;i<brackets.length();i++)
    if (brackets[i]=='<')
    count+=1;
    else if (brackets[i]=='>')
    count-=1;
    if (count==0)
    return true;
    else
    return false;
}


