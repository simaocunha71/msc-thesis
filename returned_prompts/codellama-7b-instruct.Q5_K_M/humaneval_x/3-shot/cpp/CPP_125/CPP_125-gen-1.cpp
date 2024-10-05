    vector<string> words;
    if (txt.find(" ")!=string::npos)
    {
        words.push_back(" ");
        txt.erase(remove(txt.begin(), txt.end(), ' '), txt.end());
        words=txt;
        return words;
    }
    else if (txt.find(",")!=string::npos)
    {
        words.push_back(",");
        txt.erase(remove(txt.begin(), txt.end(), ','), txt.end());
        words=txt;
        return words;
    }
    else
    {
        int c=0;
        for (int i=0;i<26;i++)
        {
            c+=txt[i];
        }
        words.push_back(to_string(c));
        return words;
    }
}



