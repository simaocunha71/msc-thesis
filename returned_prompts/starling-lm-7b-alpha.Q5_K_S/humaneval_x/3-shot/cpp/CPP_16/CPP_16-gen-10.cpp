    vector<char> all_chars;
    int i,j;
    for (i=0;i<str.length();i++)
    {
        char chr=str[i];
        if (chr<='z' && chr>='a')
        {
            chr-='a';
            chr+='A';
        }
        for (j=0;j<all_chars.size();j++)
        {
            if (all_chars[j]==chr)
                break;
        }
        if (j==all_chars.size())
            all_chars.push_back(chr);
    }
    return all_chars.size();
}


