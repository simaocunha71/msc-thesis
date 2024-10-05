    string new_str;
    string chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (find(c.begin(),c.end(),chr)==c.end())
        new_str+=chr;
    }
    if (new_str==reverse(new_str.begin(),new_str.end()))
    return {"True"};
    else
    return {"False"};
}

