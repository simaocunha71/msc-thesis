    vector<char> unique_chars;
    for (int i=0;i<str.length();i++)
    {
    if (find(unique_chars.begin(), unique_chars.end(), str[i])==unique_chars.end())
        unique_chars.push_back(str[i]);
    }
    return unique_chars.size();
}



