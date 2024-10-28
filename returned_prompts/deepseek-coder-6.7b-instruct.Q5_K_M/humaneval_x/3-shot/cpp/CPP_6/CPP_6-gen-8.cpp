    vector<int> levels;
    int level = 0;
    int max_level = 0;
    for(auto c : paren_string){
        if(c == '(') {
            level++;
            if(level > max_level)
                max_level = level;
        }
        else if(c == ')')
            level--;
    }
    levels.push_back(max_level);
    return levels;
}

