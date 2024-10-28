    string result;
    string word;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            result+=s[i];
            continue;
        }
        word+=s[i];
        sort(word.begin(),word.end());
        result+=word;
        word="";
    }
    return result;
}