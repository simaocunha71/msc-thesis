vector<string> result;
string temp = "";
for(int i = 0; i < paren_string.length(); i++){
    if(paren_string[i] == '('){
        if(temp != ""){
            result.push_back(temp);
            temp = "";
        }
    }else if(paren_string[i] == ')'){
        temp += '(';
        temp += ')';
    }else{
        temp += paren_string[i];
    }
}
if(temp != ""){
    result.push_back(temp);
}
return result;
}
int main(){
    string input = "( ) (( )) (( )( ))";
    vector<string> output = separate_paren_groups(input);
    for(auto s : output){
        cout << s << endl;
    }
    return 0;
}
