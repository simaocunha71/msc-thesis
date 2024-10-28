    vector<char> all_chars;
    char chr;
    int i;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (find(all_chars.begin(),all_chars.end(),chr)==all_chars.end())
        {
            all_chars.push_back(chr);
        }
    }
    return all_chars.size();
}



