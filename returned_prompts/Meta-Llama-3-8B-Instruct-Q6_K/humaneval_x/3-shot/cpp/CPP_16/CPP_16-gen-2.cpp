    vector<char> char_set;
    for (int i=0;i<str.length();i++)
    {
        char chr=str[i];
        if (isalpha(chr))
        {
            chr=toupper(chr);
            if (find(char_set.begin(),char_set.end(),chr)==char_set.end())
            {
                char_set.push_back(chr);
            }
        }
    }
    return char_set.size();
}
// This function converts the string to upper case before counting distinct characters. This is because it was asked to consider characters regardless of case. If the case was to be considered, we could directly push the character to the set without any conversion. The function 'find' is used to check if a character already exists in the set. If the character does not exist in the set, it is added to the set. Finally, the size of the set is returned, which gives the number of distinct characters in the string.