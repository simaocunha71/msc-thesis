    vector<string> result;
    string word;
    for (string::iterator it=s.begin();it!=s.end();)
    {
        if (*it==' ')
        {
            if (word.length()>0)
            {
                int cons=0;
                for (int i=0;i<word.length();i++)
                {
                    if (isalpha(word[i]))
                    {
                        if (tolower(word[i])!='a'&&tolower(word[i])!='e'&&tolower(word[i])!='i'&&tolower(word[i])!='o'&&tolower(word[i])!='u')
                        cons++;
                    }
                }
                if (cons==n)
                result.push_back(word);
                word="";
            }
            it++;
        }
        else
        {
            word+=*it;
            it++;
        }
    }
    if (word.length()>0)
    {
        int cons=0;
        for (int i=0;i<word.length();i++)
        {
            if (isalpha(word[i]))
            {
                if (tolower(word[i])!='a'&&tolower(word[i])!='e'&&tolower(word[i])!='i'&&tolower(word[i])!='o'&&tolower(word[i])!='u')
                cons++;
            }
        }
        if (cons==n)
        result.push_back(word);
    }
    sort(result.begin(),result.end());
    return result;
}
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H
#endif  // Q_H