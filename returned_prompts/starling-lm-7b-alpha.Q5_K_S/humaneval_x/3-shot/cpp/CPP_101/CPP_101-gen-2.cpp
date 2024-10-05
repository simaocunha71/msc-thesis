    vector<string> words;
    int i,j;
    char chr;
    for (i=0;i<s.length();i++)
    {
        chr=s[i];
        if (chr==',' || chr==' ')
        {
            words.push_back(s.substr(j,i-j));
            j=i+1;
        }
    }
    return words;
}



