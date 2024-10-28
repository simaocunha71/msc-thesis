    vector<string> words;
    string temp="";
    for(int i=0;i<s.length();i++)
    {
        if(s[i]==' '||s[i]==',')
        {
            if(temp.length()>0)
            {
                words.push_back(temp);
                temp="";
            }
        }
        else
        {
            temp+=s[i];
        }
    }
    if(temp.length()>0)
    {
        words.push_back(temp);
    }
    return words;
}


