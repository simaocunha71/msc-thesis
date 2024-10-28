    vector<char> all_chars;
    for (int i=0;i<str.length();i++)
    all_chars.push_back(tolower(str[i]));

    sort(all_chars.begin(),all_chars.end());
    all_chars.erase(unique(all_chars.begin(),all_chars.end()),all_chars.end());
    return all_chars.size();
}


