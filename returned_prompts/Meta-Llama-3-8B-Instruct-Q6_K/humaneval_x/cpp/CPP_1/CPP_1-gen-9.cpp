    vector<string> result;
    string curr_str = "";
    int count = 0;

    for(int i = 0; i < paren_string.length(); i++){
        if(paren_string[i] == '('){
            count++;
            curr_str += paren_string[i];
        }
        else if(paren_string[i] == ')'){
            count--;
            curr_str += paren_string[i];
            if(count == 0){
                result.push_back(curr_str);
                curr_str = "";
            }
        }
    }
    return result;
}
int main(){
    string input = "( ) (( )) (( )( ))";
    vector<string> output = separate_paren_groups(input);
    for(int i = 0; i < output.size(); i++){
        cout << output[i] << endl;
    }
    return 0;
}
