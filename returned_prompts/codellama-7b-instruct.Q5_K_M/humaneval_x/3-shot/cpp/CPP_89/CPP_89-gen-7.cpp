    string encrypted_string="";
    int i;
    for (i=0;i<s.length();i++)
    {
        if (s[i]=='z')
        encrypted_string+=s[i-26]+s[i-26];
        else
        encrypted_string+=s[i]+s[i]+s[i];
    }
    return encrypted_string;
}


