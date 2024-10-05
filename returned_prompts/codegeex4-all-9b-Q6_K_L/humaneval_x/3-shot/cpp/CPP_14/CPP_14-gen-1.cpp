    vector<string> all_pre;
    string current_pre;
    int i;
    for (i=0;i<=str.length();i++)
    {
        current_pre=str.substr(0,i);
        all_pre.push_back(current_pre);
    }
    return all_pre;
}

