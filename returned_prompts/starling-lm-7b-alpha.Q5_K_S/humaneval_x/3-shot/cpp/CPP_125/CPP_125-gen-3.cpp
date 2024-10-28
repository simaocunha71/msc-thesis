    vector<string> words;
    int i;
    for (i=0;i<txt.length();i++)
    if (txt[i]!=' ' && txt[i]!=',' && txt[i]!='.')
    {
        string current_word="";
        while (i<txt.length())
        {
            current_word+=txt[i];
            if (txt[i]==' ' || txt[i]==',' || txt[i]=='.')
            {
                words.push_back(current_word);
                break;
            }
            i+=1;
        }
    }
    return words;
}

