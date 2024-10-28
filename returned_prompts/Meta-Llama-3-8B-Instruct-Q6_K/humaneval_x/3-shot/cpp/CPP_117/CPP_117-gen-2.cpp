    vector<string> result;
    string word;
    int count=0;
    for (int i=0;i<s.length();i++)
    {
        if (isalpha(s[i]))
        {
            if (s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u')
                continue;
            word+=s[i];
            count++;
        }
        else if (word.length()>0)
        {
            if (count==n)
            {
                result.push_back(word);
            }
            word="";
            count=0;
        }
    }
    if (word.length()>0 && count==n)
    {
        result.push