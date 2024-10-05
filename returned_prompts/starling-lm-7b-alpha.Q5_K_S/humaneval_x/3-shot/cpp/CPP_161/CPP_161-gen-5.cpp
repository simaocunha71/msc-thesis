    int i;
    string result="";
    for (i=0;i<s.length();i++)
    {
        if (s[i]>='a'&&s[i]<='z')
        result+=char(s[i]-'a'+'A');
        else if (s[i]>='A'&&s[i]<='Z')
        result+=char(s[i]-'A'+'a');
        else
        result+=s[i];
    }
    return result;
}


