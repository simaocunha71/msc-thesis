    int count=0;
    int i;
    for (i=0;i<s.length();i+=2)
    if (toupper(s[i])=='A'||toupper(s[i])=='E'||toupper(s[i])=='I'||toupper(s[i])=='O'||toupper(s[i])=='U')
    count+=1;
    return count;
}


