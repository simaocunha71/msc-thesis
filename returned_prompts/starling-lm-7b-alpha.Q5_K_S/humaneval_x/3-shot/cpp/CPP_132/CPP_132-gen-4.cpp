    int i,level;
    for (i=0;i<str.length();i++)
    {
        if (str[i]=='[')
        level+=1;
        if (str[i]==']')
        level-=1;
        if (level<0)
        return true;
    }
    return level==0;
}



