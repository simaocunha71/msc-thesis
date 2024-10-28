    vector<int> result;
    int level = 0;
    int max_level = 0;
    int current_level = 0;
    for(int i = 0; i < paren_string.size(); i++){
        if(paren_string[i] == '('){
            level++;
            if(max_level < level){
                max_level = level;
            }
        }
        else if(paren_string[i] == ')'){
            level--;
        }
    }
    return result;
}
