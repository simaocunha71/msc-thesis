    vector<string> all_prefix;
    string current_str;
    int i;
    for (i=0;i<str.length();i++)
    {
        current_str+=str[i];
        all_prefix.push_back(current_str);
    }
    return all_prefix;
}

