    int i;
    int count=0;
    for (i=0;i<s.length();i+=2)
    if (s[i]>='A' && s[i]<='Z')
    count++;
    return count;
}


