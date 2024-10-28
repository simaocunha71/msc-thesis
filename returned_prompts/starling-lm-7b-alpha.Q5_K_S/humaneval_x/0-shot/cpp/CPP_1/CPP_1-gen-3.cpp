    vector<string> ret;
    int i = 0;
    string cur = "";
    while(i < paren_string.size()){
        if(paren_string[i] == '('){
            cur += paren_string[i];
        }else if(paren_string[i] == ')'){
            if(cur.size() == 0){
                cur += paren_string[i];
            }else if(cur.back() == '('){
                cur = cur.substr(0, cur.size()-1);
                cur += paren_string[i];
            }else{
                ret.push_back(cur);
                cur = "";
                cur += paren_string[i];
            }
        }
        ++i;
    }
    if(cur.size() > 0){
        ret.push_back(cur);
    }
    return ret;
}

int main(){
    printf("%s\n", separate_paren_groups("( ) (( )) (( )( ))").c_str());
}





























































































































































































































































