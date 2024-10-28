    vector<int> levels;
    string current_paren;
    int level=0;
    int i;
    for (i=0;i<paren_string.length();i++)
    {
        if (paren_string[i]=='(')
        {
        level+=1;
        current_paren+=paren_string[i];
        }
        if (paren_string[i]==')')
        {
            level-=1;
            current_paren+=paren_string[i];
            if (level==0){
                levels.push_back(current_paren.length());
                current_paren="";
            }
        }
    }
    return levels;
}



