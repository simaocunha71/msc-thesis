    string result="";
    for (int i=0;i<s.length();i++)
    {
        char chr=s[i];
        if (c.find(chr)==string::npos)
        result+=chr;
    }
    if (result==string(result.rbegin(),result.rend()))
    return {result,"True"};
    else
    return {result,"False"};
}

