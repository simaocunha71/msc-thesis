    vector<int> max_level;
    string current_paren;
    int level=0;
    int max_lvl;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        if (paren_string[i]=='(')
        {
            level+=1;
            current_paren+=paren_string[i];
        }
        else if (paren_string[i]==')')
        {
            level-=1;
            current_paren+=paren_string[i];
            if (level==0){
                max_lvl=0;
                for (int j=0;j<current_paren.length();j++)
                {
                    if (current_paren[j]=='(')
                    max_lvl+=1;
                }
                max_level.push_back(max_lvl);
                current_paren="";
            }
        }
    }
    return max_level;
}


