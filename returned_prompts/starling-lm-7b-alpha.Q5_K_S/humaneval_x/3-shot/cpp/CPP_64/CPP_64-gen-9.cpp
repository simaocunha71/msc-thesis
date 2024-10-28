    int i,count=0;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr=='a'||chr=='e'||chr=='i'||chr=='o'||chr=='u')
        count+=1;
        if (chr=='y'&&i==s.length()-1)
        count+=1;
    }
    return count;
}


