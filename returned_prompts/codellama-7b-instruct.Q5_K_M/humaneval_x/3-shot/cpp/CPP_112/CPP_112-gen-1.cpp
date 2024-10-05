    vector<string> ans;
    string result;
    bool is_palindrome;
    for(int i=0;i<s.length();i++)
    {
        if(!find(c.begin(),c.end(),s[i]))
            result+=s[i];
    }
    is_palindrome=result==string(result.rbegin(),result.rend());
    ans.push_back(result);
    ans.push_back(is_palindrome?"True":"False");
    return ans;
}


