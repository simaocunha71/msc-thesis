    vector<char> chars;
    char chr;
    int i;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        if (find(chars.begin(),chars.end(),chr)==chars.end())
        {
            chars.push_back(chr);
        }
    }
    return chars.size();
}


