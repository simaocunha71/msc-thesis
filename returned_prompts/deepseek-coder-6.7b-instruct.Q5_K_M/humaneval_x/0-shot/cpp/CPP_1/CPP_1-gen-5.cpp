    vector<string> paren_groups;
    int start = 0;
    int open_count = 0;
    for(int i=0; i<paren_string.size(); i++){
        if(paren_string[i] == '('){
            open_count++;
        }
        else if(paren_string[i] == ')'){
            open_count--;
            if(open_count == 0){
                paren_groups.push_back(paren_string.substr(start, i-start+1));
                start = i+1;
            }
        }
    }
    return paren_groups;
}

int main(){
    string test_string = "(  )  (( ))  (( )( ))";
    vector<string> result = separate_paren_groups(test_string);
    for(int i=0; i<result.size(); i++){
        cout<<result[i]<<endl;
    }
    return 0;
}
*/

//src/main/resources/cpp/separate_paren_groups_2.cpp
/*
