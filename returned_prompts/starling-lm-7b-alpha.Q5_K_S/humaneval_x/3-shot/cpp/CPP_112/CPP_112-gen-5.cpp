    string new_str;
    char chr;
    int i;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (find(c.begin(),c.end(),chr)==c.end())
        {
            new_str+=chr;
        }
    }
    return {new_str,new_str==string(new_str.rbegin(),new_str.rend())};
}


