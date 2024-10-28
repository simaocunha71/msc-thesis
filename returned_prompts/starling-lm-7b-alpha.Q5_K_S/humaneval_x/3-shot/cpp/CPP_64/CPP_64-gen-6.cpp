    int result=0;
    for (int i=0;i<s.length();i++)
    if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||(s[i]=='y'&&i==s.length()-1))
    result+=1;

    return result;
}




