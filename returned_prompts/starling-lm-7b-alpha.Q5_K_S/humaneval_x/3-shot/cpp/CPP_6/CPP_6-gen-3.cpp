    vector<int> all_levels;
    int current_level=0;
    char chr;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        chr=paren_string[i];
        if (chr=='(')
        {
            current_level+=1;
        }
        if (chr==')')
        {
            current_level-=1;
        }
        if (i==paren_string.length()-1 || paren_string[i+1]==' '){
            all_levels.push_back(current_level);
            current_level=0;
        }
    }
    return all_levels;
}




