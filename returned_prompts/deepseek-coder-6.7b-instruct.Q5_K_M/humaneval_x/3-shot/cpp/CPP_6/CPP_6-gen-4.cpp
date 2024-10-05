    vector<int> levels;
    int level = 0, max_level = 0;
    char chr;
    int i;
    for  (i=0; i<paren_string.length(); i++)
    {
        chr = paren_string[i];
        if  (chr == '(')
        {
            level += 1;
            if  (level > max_level)
            {
                max_level = level;
            }
        }
        else if  (chr == ')')
        {
            level -= 1;
        }
    }
    levels.push_back(max_level);
    return levels;
}


