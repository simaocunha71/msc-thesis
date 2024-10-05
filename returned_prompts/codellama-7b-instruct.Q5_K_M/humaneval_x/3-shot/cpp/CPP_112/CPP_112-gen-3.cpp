    vector<string> result;
    string result_string;
    bool palindrome=true;
    for (int i=0;i<s.length();i++)
    {
        if (find(c.begin(),c.end(),s[i])==c.end())
        {
            result_string+=s[i];
        }
    }
    for (int i=result_string.length()-1;i>=0;i--)
    {
        if (result_string[i]!=result_string[0])
        {
            palindrome=false;
        }
    }
    result.push_back(result_string);
    result.push_back(palindrome?"True":"False");
    return result;
}

