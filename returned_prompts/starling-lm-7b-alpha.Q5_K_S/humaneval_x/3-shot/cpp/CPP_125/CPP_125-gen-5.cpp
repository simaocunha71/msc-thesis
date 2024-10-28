    vector<string> all_words;
    char chr;
    bool space_found=false;
    int i;
    for (i=0;i<txt.length();i++)
    {
        chr=txt[i];
        if (chr==' ')
        {
            space_found=true;
        }
        if (space_found || chr==',')
        {
            all_words.push_back(txt.substr(0,i));
            txt=txt.substr(i+1);
            space_found=false;
        }
    }
    if (txt.length()!=0)
    {
        all_words.push_back(txt);
    }
    return all_words;
}


