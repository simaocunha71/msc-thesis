vector<string> result;
string cur_string = "";
for(int i = 0; i < paren_string.length(); i++){
    if(paren_string[i] == '('){
        if(cur_string.length() > 0){
            result.push_back(cur_string);
            cur_string = "";
        }
    }else if(paren_string[i] == ')'){
        if(cur_string.length() > 0){
            cur_string += ")";
        }
    }else{
        cur_string += paren_string[i];
    }
}
if(cur_string.length() > 0){
    result.push_back(cur_string);
}
return result;
}

B:
vector<string> separate_paren_groups(string paren_string){
    vector<string> result;
    string cur_string = "";
    int open_count = 0;
    for(char c: paren_string){
        if(c == '('){
            open_count++;
        }else if(c == ')'){
            open_count--;
            if(open_count == 0){
                result.push_back(cur_string + ")");
                cur_string = "";
            }else{
                cur_string += ")";
            }
        }else{
            if(open_count > 0){
                cur_string += c;
            }else{
                result.push_back(cur_string);
                cur_string = c;
            }
        }
    }
    if(open_count > 0){
        result.push_back(cur_string);
    }
    return result;
}

C:
vector<string> separate_paren_groups(string paren_string){
    vector<string> result;
    stack<string> s;
    string cur_string = "";
    for(char c: paren_string){
        if(c == '('){
            cur_string += c;
            s.push(cur_string);
            cur_string = "";
        }else if(c == ')'){
            cur_string += c;
            if(!s.empty()){
                string temp = s.top();
                s.pop();
                temp += cur_string;
                result.push_back(temp);
                cur_string = "";
            }
        }else{
            cur_string += c;
        }
    }
    if(!s.empty()){
        while(!s.empty()){
            result.push_back(s.top());
            s.pop();
        }
    }
    return result;
}

D:
vector<string> separate_paren_groups(string paren_string){
    vector<string> result;
    string cur_string = "";
    for(int i = 0; i < paren_string.length(); i++){
        if(paren_string[i] == '('){
            cur_string += "(";
        }else if(paren_string[i] == ')'){
            if(cur_string.length() >