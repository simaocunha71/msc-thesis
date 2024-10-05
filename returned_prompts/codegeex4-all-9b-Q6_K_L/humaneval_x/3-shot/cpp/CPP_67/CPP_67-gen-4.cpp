    int i;
    string s1="",s2="";
    int num1,num2;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='a')
        {
            int j=i+1;
            while(s[j]!=' ')
                s1+=s[j++];
        }
        if (s[i]=='o')
        {
            int j=i+1;
            while(s[j]!=' ')
                s2+=s[j++];
        }
    }
    num1=atoi(s1.c_str());
    num2=atoi(s2.c_str());
    return n-num1-num2;
}

