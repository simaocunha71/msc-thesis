    int i;
    string result;
    for (i=0;i<str.length();i++)
    {
        if (str[i]>='A'&&str[i]<='Z')
        result+=str[i]+32;
        else if (str[i]>='a'&&str[i]<='z')
        result+=str[i]-32;
    }
    return result;
}


