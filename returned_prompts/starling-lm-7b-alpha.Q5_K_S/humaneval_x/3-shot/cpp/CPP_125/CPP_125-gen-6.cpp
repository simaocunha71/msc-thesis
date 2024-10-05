    int i;
    vector<string> words;
    int first_char;
    int last_char;
    for (i=0;i<txt.length();i++)
    if (txt[i]==' '||txt[i]==',')
    {
        last_char=i;
        if (last_char==txt.length()-1)
        {
        first_char=i-1;
        words.push_back(txt.substr(first_char,last_char-first_char+1));
        }
        else
        {
        first_char=i;
        words.push_back(txt.substr(first_char,last_char-first_char+1));
        }
    }
    if (txt.length()-last_char>1&&txt[last_char+1]!=' ')
    {
        last_char+=1;
        first_char=last_char;
        words.push_back(txt.substr(first_char,last_char-first_char+1));
    }
    return words;
}







