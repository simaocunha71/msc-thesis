    vector<char> all_chars;
    string new_str=str;
    int i;
    char chr;
    for (i=0;i<str.length();i++)
    {
        chr=str[i];
        new_str.erase(remove(new_str.begin(), new_str.end(), chr), new_str.end());
        if (new_str.length()==str.length()-1)
        all_chars.push_back(chr);
        new_str=str;
    }

    return all_chars.size();
}

