    int i,count=0;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u') count++;
        if (s[i]=='y'&&i==s.length()-1) count++;
    }
    return count;
}


