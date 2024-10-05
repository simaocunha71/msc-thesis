    string result;
    string word;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            result+=s[i];
            continue;
        }
        word="";
        while (i<s.length() && s[i]!=' ')
        {
            word+=s[i];
            i++;
        }
        i--;
        sort(word.begin(),word.end());
        result+=word;
    }
    return result;
}
