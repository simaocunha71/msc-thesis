    vector<int> result;
    for(int i=0; i<paren_string.size(); i++){
        int depth = 0;
        for(int j=i; j<paren_string.size(); j++){
            if(paren_string[j] == '('){
                depth++;
            }else if(paren_string[j] == ')'){
                depth--;
                if(depth == 0){
                    result.push_back(depth);
                    i = j + 1;
                    break;
                }
            }
        }
    }
    return result;
}

