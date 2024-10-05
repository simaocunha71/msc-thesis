    int i;
    int count_left=0;
    int count_right=0;
    for (i=0;i<brackets.length();i++)
    {
        if (brackets[i]=='<')
        count_left+=1;
        if (brackets[i]=='>')
        count_right+=1;
    }
    if (count_left==count_right)
    return true;
    return false;
}



