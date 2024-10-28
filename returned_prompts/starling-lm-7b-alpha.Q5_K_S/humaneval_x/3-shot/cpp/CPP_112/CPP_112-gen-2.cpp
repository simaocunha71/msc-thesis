    vector<char> all_chars;
    for (int i=0;i<s.length();i++)
    all_chars.push_back(s[i]);

    sort(all_chars.begin(),all_chars.end());
    vector<char> all_chars_unique;
    all_chars_unique.push_back(all_chars[0]);
    for (int i=1;i<all_chars.size();i++)
    if (all_chars[i]!=all_chars[i-1])
    all_chars_unique.push_back(all_chars[i]);

    vector<string> result;
    string all_chars_unique_string;
    for (int i=0;i<all_chars_unique.size();i++)
    all_chars_unique_string+=all_chars_unique[i];

    for (int i=0;i<all_chars.size();i++)
    {
        int j;
        for (j=0;j<c.length();j++)
        if (all_chars[i]==c[j])
        break;
        if (j==c.length())
        all_chars_unique_string=all_chars_unique_string.substr(0,i)+all_chars_unique_string.substr(i+1,all_chars_unique_string.length()-(i+1))+all_chars_unique_string.substr(i);
    }

    result.push_back(all_chars_unique_string);
    string all_chars_unique_string_rev;
    for (int i=0;i<all_chars_unique_string.length();i++)
    all_chars_unique_string_rev+=all_chars_unique_string[all_chars_unique_string.length()-1-i];

    result.push_back(all_chars_unique_string_rev);

    int i=0;
    while (i<all_chars_unique_string.length()&&all_chars_unique_string[i]==all_chars_unique_string_rev[i])
    i++;
    if (i==all_chars