    int count=0;
    int i;
    for (i=0;i<s.length();i+=2)
    if (isupper(s[i]))
    count+=1;
    return count;
}


