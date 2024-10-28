    string new_s;
    vector<string> result;
    int i,j;
    for (i=0;i<s.length();i++)
    {
        bool found=false;
        for (j=0;j<c.length();j++)
        {
            if (s[i]==c[j])
            {
                found=true;
                break;
            }
        }
        if (!found)
        new_s+=s[i];
    }
    result.push_back(new_s);
    result.push_back(is_palindrome(new_s)? "True":"False");
    return result;
}

bool is_palindrome(string s){
    int i,j;
    for (i=0;i<s.length();i++)
    {
        if (s[i]!=s[s.length()-i-1])
        return false;
    }
    return true;
}


