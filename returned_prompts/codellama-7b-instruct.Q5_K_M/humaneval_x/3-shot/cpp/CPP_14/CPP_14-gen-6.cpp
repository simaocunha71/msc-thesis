    vector<string> all_prefixes_str;
    int i;
    for (i=0;i<str.length();i++)
    {
        string current_prefix=str.substr(0,i+1);
        all_prefixes_str.push_back(current_prefix);
    }
    return all_prefixes_str;
}



