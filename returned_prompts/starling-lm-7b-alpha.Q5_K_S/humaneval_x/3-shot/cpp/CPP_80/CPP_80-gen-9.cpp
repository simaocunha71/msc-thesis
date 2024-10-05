    if (s.length()<3)
    return false;
    vector<char> chars;
    int i;
    for (i=0;i<3;i++)
    chars.push_back(s[i]);
    for (i=3;i<s.length();i++)
    if (chars.end()!=find(chars.begin(),chars.end(),s[i]))
    return false;
    chars.push_back(s[i]);
    return true;
}




