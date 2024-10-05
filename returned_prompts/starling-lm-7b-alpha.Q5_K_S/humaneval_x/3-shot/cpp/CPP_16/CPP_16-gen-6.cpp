    int i;
    vector<char> str_set;
    for (i=0;i<str.length();i++)
    {
        char chr=tolower(str[i]);
        if (find(str_set.begin(), str_set.end(), chr)==str_set.end())
        {
            str_set.push_back(chr);
        }
    }
    return str_set.size();
}


