    int i;
    int lvl=0;
    char chr;
    for (i=0;i<brackets.length();i++)
    {
        chr=brackets[i];
        if (chr=='<')
        {
            lvl+=1;
        }
        if (chr=='>')
        {
            lvl-=1;
            if (lvl<0)
            return false;
        }
    }
    if (lvl!=0)
    return false;
    else
    return true;
}



