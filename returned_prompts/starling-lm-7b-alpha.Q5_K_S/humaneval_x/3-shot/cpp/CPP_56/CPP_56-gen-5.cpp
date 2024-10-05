    int i;
    int less_count=0;
    int more_count=0;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
        {
        less_count+=1;
        }
        if (brackets[i]=='>')
        {
        if (less_count>0)
        {
        less_count-=1;
        more_count+=1;
        }
        else
        {
        return false;
        }
        }
    }
    if (less_count!=0 || more_count!=0)
    return false;
    else
    return true;
}


