    vector<string> prefixes;
    string temp;
    int i;
    for (i=0;i<str.length();i++)
    {
        temp=str.substr(0,i+1);
        prefixes.push_back(temp);
    }
    return prefixes;
}

