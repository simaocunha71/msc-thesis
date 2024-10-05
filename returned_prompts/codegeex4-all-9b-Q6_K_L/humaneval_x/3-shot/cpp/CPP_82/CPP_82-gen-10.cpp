    int i,level;
    level=str.length();
    if (level==1)
    return false;
    for (i=2;i<=level/2;i++)
    if (level%i==0)
    return false;
    return true;
}

