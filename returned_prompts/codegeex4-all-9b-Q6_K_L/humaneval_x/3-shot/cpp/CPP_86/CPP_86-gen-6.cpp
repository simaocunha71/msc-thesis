    int i;
    string words;
    string current_word;
    for (i=0;i<s.length();i++)
    {
        if (s[i]==' ')
        {
            sort(current_word.begin(), current_word.end());
            words+=current_word;
            words+=' ';
            current_word="";
        }
        else
            current_word+=s[i];
    }
    sort(current_word.begin(), current_word.end());
    words+=current_word;
    return words;
}

