    vector<string> all;
    int i;
    for (i=1;i<=str.length();i++)
    {
        all.push_back(str.substr(0,i));
    }
    return all;
}

