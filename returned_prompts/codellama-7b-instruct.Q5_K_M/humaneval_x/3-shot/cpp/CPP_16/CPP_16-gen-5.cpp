    transform(str.begin(), str.end(), str.begin(), ::toupper);
    vector<int> seen(256, 0);
    for (int i=0;i<str.length();i++)
    seen[str[i]] = 1;
    return seen.size();
}


