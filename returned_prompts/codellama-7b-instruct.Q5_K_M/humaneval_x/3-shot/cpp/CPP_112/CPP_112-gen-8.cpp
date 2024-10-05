    vector<string> result;
    string result_string;
    bool check=true;
    for (int i=0;i<s.length();i++)
    {
        if (find(c.begin(),c.end(),s[i])==c.end())
        result_string+=s[i];
        else check=false;
    }
    if (result_string.empty()) check=false;
    for (int i=result_string.length()-1;i>=0;i--)
    result_string+=result_string[i];
    result.push_back(result_string);
    if (result_string.empty()) check=false;
    result.push_back(to_string(check));
    return result;
}


