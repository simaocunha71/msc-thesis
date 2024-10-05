    string result="";
    for (int i=0;i<s.length();i++)
    {
        if (s[i] != c[0])
        result+=s[i];
    }
    if (result==string(result.rbegin(),result.rend()))
    return {result,"True"};
    else
    return {result,"False"};
}

