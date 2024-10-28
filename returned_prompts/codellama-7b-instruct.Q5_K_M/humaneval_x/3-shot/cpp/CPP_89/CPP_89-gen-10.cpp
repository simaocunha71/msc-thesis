    string encrypted="";
    for (int i=0;i<s.length();i++)
    {
        if (s[i]>='a' && s[i]<='z')
        encrypted+=s[i]+2*2;
        if (s[i]>='A' && s[i]<='Z')
        encrypted+=s[i]+2*2;
        if (s[i]==' ')
        encrypted+=' ';
    }
    return encrypted;
}




