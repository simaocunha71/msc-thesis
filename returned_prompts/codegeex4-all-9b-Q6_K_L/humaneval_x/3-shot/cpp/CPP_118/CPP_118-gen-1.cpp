    int i;
    for (i=word.length()-1;i>=0;i--)
    {
    if (word[i]=='a'||word[i]=='e'||word[i]=='i'||word[i]=='o'||word[i]=='u')
    if (word[i-1]!='a'||word[i-1]!='e'||word[i-1]!='i'||word[i-1]!='o'||word[i-1]!='u')
    return word[i];
    }
    return "";
}

