    vector<string> result;
    string word;
    int i, consonants=0;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            if (consonants==n)
                result.push_back(word);
            word="";
            consonants=0;
        }
        else
        {
            if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'||s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U')
                continue;
            word+=s[i];
            consonants++;
        }
    }
    if (consonants==n)
        result.push_back(word);
    sort(result.begin(),result.end());
    return result;
}