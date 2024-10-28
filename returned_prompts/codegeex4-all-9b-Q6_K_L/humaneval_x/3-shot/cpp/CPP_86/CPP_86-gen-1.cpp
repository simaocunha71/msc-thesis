    string new_s="";
    string word="";
    int i;
    for (i=0;i<s.length();i++)
    {
    if (s[i]==' ')
    {
        sort(word.begin(),word.end());
        new_s+=word+" ";
        word="";
    }
    else
    word+=s[i];
    }
    sort(word.begin(),word.end());
    new_s+=word;
    return new_s;
}

