    vector<int> levels;
    for(int i=0; i<paren_string.length(); i++){
        if(paren_string[i] == '('){
            int level = 1;
            for(int j=i+1; j<paren_string.length(); j++){
                if(paren_string[j] == '('){
                    level++;
                }
                else if(paren_string[j] == ')'){
                    level--;
                    if(level == 0){
                        levels.push_back(level);
                        break;
                    }
                }
            }
        }
    }
    return levels;
}

B:
    vector<int> levels;
    int max_level = 0;
    int current_level = 0;
    for(char c : paren_string){
        if(c == '('){
            current_level++;
            if(current_level > max_level){
                max_level = current_level;
            }
        }
        else if(c == ')'){
            current_level--;
        }
    }
    levels.push_back(max_level);
    return levels;
}

C:
    vector<int> levels;
    int current_level = 0;
    int max_level = 0;
    for(char c : paren_string){
        if(c == '('){
            current_level++;
            if(current_level > max_level){
                max_level = current_level;
            }
        }
        else if(c == ')'){
            current_level--;
        }
    }
    for(int i=paren_string.length()-1; i>=0; i--){
        if(paren_string[i] == '('){
            current_level++;
            if(current_level > max_level){
                max_level = current_level;
            }
        }
        else if(paren_string[i] == ')'){
            current_level--;
        }
    }
    levels.push_back(max_level);
    return levels;
}

D:
    vector<int> levels;
    int current_level = 0;
    int max_level = 0;
    for(char c : paren_string){
        if(c == '('){
            current_level++;
            if(current_level > max_level){
                max_level = current_level;
            }
        }
        else if(c == ')'){
            current_level--;
        }
    }
    levels.push_back(max_level);
    for(int i=paren_string.length()-1; i>=0; i--){
        if(paren_string[i] == '('){
            current_level++;
        }
        else if(paren_string[i] == ')'){
            current_level--;
            if(current_level == 0){
                levels.push_back(current_level);
            }
        }
    }
    reverse(levels.begin(), levels.end());
