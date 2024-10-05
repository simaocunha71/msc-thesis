    int i;
    int c=0;
    for (i=0;i<str.length();i++)
    if (str[i]=='[')
    c+=1;
    if (c%2==1)
    return true;
    return false;
}


