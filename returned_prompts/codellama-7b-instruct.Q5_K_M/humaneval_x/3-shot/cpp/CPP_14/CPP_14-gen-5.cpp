    vector<string> all_prefixes_vec;
    int i;
    for (i=0;i<str.length();i++)
    {
        string prefix=str.substr(0,i+1);
        all_prefixes_vec.push_back(prefix);
    }
    return all_prefixes_vec;
}




