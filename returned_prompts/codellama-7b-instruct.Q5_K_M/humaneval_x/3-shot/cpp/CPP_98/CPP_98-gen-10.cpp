    int count=0;
    int i;
    for (i=0;i<s.length();i+=2)
    if (s[i]>='A' && s[i]<='Z')
    count+=1;
    return count;
}


