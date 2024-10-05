    int i;
    for (i=0;i<str.length();i++)
    if (str[i]>=65 && str[i]<=90)
    str[i]+=32;
    else if (str[i]>=97 && str[i]<=122)
    str[i]-=32;
    return str;
}

