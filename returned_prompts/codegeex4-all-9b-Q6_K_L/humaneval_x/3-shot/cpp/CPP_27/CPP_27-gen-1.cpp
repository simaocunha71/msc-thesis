    string new_str;
    int i;
    for (i=0;i<str.length();i++)
    {
        if (str[i]<='z' && str[i]>='a')
        new_str+=char(str[i]-32);
        if (str[i]<='Z' && str[i]>='A')
        new_str+=char(str[i]+32);
        if (str[i]>='0' && str[i]<='9')
        new_str+=str[i];
    }
    return new_str;
}

