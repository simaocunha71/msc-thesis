    string result="";
    int len=s.length();
    for (int i=0;i<len;i++)
    {
        if (s[i]=='z')
        result+=('a'+2*(i%2));
        else
        result+=s[i]+2*(i%2);
    }
    return result;
}


