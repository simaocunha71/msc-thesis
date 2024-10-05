    char chr;
    int i;
    string result="";
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        result+=chr;
    }
    sort(result.begin(),result.end());
    return result;
}



