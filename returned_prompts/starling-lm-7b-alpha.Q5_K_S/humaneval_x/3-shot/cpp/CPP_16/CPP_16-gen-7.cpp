    vector<char> all_chars;
    char chr;
    int i;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        all_chars.push_back(chr);
    }
    sort(all_chars.begin(),all_chars.end());
    return all_chars.size();
}


