    vector<string> all_words;
    int i=0;
    while (i<s.length())
    {
        if (s[i]==' '||s[i]==',')
        i++;
        else
        {
            int j=i;
            while (s[j]!=' '&&s[j]!=','&&j<s.length())
            j++;
            all_words.push_back(s.substr(i,j-i));
            i=j;
        }
    }
    return all_words;
}


