    vector<string> v;
    vector<string>::iterator it;
    string word;
    int count;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]!=' ')
        {
            word+=s[i];
        }
        else
        {
            count=0;
            for (int j=0;j<word.length();j++)
            {
                if (word[j]!='a'&&word[j]!='e'&&word[j]!='i'&&word[j]!='o'&&word[j]!='u')
                count++;
            }
            if (count==n)
            v.push_back(word);
            word="";
        }
    }
    return v;
}





