    string result;
    bool is_letter=true;
    for (int i=0;i<s.length();i++)
    {
        if (!isalpha(s[i]))
        {
            result+=s[i];
            is_letter=false;
        }
        else
        {
            if (is_letter)
                result+=tolower(s[i]);
            else
                result+=toupper(s[i]);
            is_letter=true;
        }
    }
    if (result.length()==0)
        result=s.substr(1)+s[0];
    return result;
}

