    vector<int> result;
    stack<int> s;
    for(int i=0; i<paren_string.length(); i++){
        if(paren_string[i] == '('){
            s.push(i);
        }
        else if(paren_string[i] == ')'){
            s.pop();
            if(s.empty()){
                result.push_back(1);
            }
            else{
                result.push_back(s.top() - i);
            }
        }
    }
    return result;
}

