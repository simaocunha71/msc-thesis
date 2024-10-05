    vector<string> all;
    string str1;
    int i;
    for (i=0;i<str.length();i++)
    {
        str1=str.substr(0,i);
        all.push_back(str1);
    }
    return all;
}

