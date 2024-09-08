    //split the string by comma or space
    vector<string> result;
    string word = "";
    for(int i = 0; i < s.length(); i++){
        if(s[i] == ',' || s[i] == ' '){
            if(word != ""){
                result.push_back(word);
                word = "";
            }
        }else{
            word += s[i];
        }
    }
    if(word != ""){
        result.push_back(word);
    }
    return result;
}

int main(){
    string s = "Hi, my name is John";
    vector<string> res = words_string(s);
    for(auto i : res){
        printf("%s\n", i.c_str());
    }
    return 0;
}

