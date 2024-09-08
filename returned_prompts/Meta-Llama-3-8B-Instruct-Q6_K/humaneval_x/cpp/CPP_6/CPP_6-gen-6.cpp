    int n = paren_string.length();
    vector<int> result;
    int max_level = 0;
    int current_level = 0;
    for(int i = 0; i < n; i++){
        if(paren_string[i] == '('){
            current_level++;
            max_level = max(max_level, current_level);
        } else if(paren_string[i] == ')'){
            current_level--;
        }
    }
    result.push_back(max_level);
    return result;
}
B:
    int n = paren_string.length();
    vector<int> result;
    int max_level = 0;
    for(int i = 0; i < n; i++){
        if(paren_string[i] == '('){
            int level = 1;
            while(i + 1 < n && paren_string[i+1] == '('){
                i++; level++;
            }
            max_level = max(max_level, level);
            result.push_back(level);
            i++;
        } else if(paren_string[i] == ')'){
            if(i > 0 && paren_string[i-1] == '('){
                i--;
                int level = 1;
                while(i > 0 && paren_string[i-1] == ')'){
                    i--; level++;
                }
                max_level = max(max_level, level);
                result.push_back(level);
                i--;
            }
        }
    }
    return result;
}
C:
    int n = paren_string.length();
    vector<int> result;
    for(int i = 0; i < n; i++){
        int level = 0;
        while(i < n && paren_string[i] != ' '){
            if(paren_string[i] == '('){
                level++;
            } else if(paren_string[i] == ')'){
                level--;
            }
            i++;
        }
        result.push_back(level);
    }
    return result;
}B:
    int n = paren_string.length();
    vector<int> result;
    for(int i = 0; i < n; i++){
        int level = 0;
        if(paren_string[i] == '('){
            level++;
        }
        while(i + 1 < n && paren_string[i+1] == '('){
            i++; level++;
        }
        result.push_back(level);
        i++;
    }
    return result;
}

D:
    int n = paren_string.length();
    vector<int> result;
    for(int i = 0; i < n; i++){
        int level = 0