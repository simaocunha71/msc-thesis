    int i,count=0;
    char chr;
    for (i=0;i<s.length();i+=2)
    {
        chr=s[i];
        if (chr=='A'||chr=='E'||chr=='I'||chr=='O'||chr=='U')
        count+=1;
    }
    return count;
}


