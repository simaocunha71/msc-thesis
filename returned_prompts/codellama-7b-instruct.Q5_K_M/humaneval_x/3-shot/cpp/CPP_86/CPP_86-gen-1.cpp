    int i;
    string new_string;
    string word;
    string temp_word;
    bool is_first=true;
    for (i=0;i<s.length();i++)
    {
        if (s[i]!=' ')
        {
            word+=s[i];
        }
        else
        {
            if (is_first==true)
            {
                is_first=false;
                new_string+=word;
            }
            else
            {
                new_string+=" ";
                new_string+=word;
            }
            sort(word.begin(),word.end());
            word="";
        }
    }
    if (is_first==true)
    {
        new_string+=word;
    }
    else
    {
        new_string+=" ";
        new_string+=word;
    }
    sort(new_string.begin(),new_string.end());
    return new_string;
}



