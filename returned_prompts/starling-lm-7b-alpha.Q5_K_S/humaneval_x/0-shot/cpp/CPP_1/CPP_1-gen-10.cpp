    vector<string> paren_groups;
    int level = 0;
    int pos = 0;
    while(pos < paren_string.size()){
        if(paren_string[pos] == '('){
            level++;
        }else if(paren_string[pos] == ')'){
            level--;
        }
        if(level == 0){
            string group = paren_string.substr(0,pos);
            paren_string = paren_string.substr(pos);
            paren_groups.push_back(group);
            pos = 0;
            goto A;
        }
        pos++;
    }
    return paren_groups;
}

int main(){
    string s = "( ) (( )) (( )( ))";
    vector<string> res = separate_paren_groups(s);
    printf("%s\n",res.size()?"(":")");
    for(int i = 0;i < res.size();i++)
        printf("%s%s","(",res[i].c_str()),printf("%s\n",")");
}























































































































































































































































