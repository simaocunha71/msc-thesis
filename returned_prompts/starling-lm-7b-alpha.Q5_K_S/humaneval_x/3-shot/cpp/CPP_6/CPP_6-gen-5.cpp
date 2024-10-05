    vector<int> all_levels;
    int curr_level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            curr_level+=1;
            if (i==paren_string.length()-1)
                all_levels.push_back(curr_level);
        }
        if (chr==')')
        {
            curr_level-=1;
        }
    }
    return all_levels;
}



