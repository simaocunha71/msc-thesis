    vector<string> prefixes;
    string current_prefix="";
    int i;
    for (i=0;i<str.length();i++)
    {
        current_prefix+=str[i];
        prefixes.push_back(current_prefix);
    }
    return prefixes;
}


