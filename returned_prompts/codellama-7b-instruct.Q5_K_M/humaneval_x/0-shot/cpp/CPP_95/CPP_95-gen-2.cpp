    if(dict.empty()){
        return false;
    }
    bool is_lower = false;
    bool is_upper = false;
    for(auto& key_val: dict){
        if(key_val.first.empty()){
            continue;
        }
        if(key_val.first.find_first_not_of("abcdefghijklmnopqrstuvwxyz") != string::npos){
            return false;
        }
        if(key_val.first.find_first_not_of("ABCDEFGHIJKLMNOPQRSTUVWXYZ") != string::npos){
            return false;
        }
        if(key_val.first.size() == 1 && key_val.first.front() >= 'A' && key_val.first.front() <= 'Z'){
            is_upper = true;
        }
        if(key_val.first.size() == 1 && key_val.first.front() >= 'a' && key_val.first.front() <= 'z'){
            is_lower = true;
        }
    }
    if(is_lower && is_upper){
        return true;
    }
    return false;
}
int main(int argc, char** argv){
    map<string,string> dict;
    dict.insert({"a","apple"});
    dict.insert({"A","banana"});
    dict.insert({"B","banana"});
    dict.insert({"Name","John"});
    dict.insert({"Age","36"});
    dict.insert({"City","Houston"});
    dict.insert({"STATE","NC"});
    dict.insert({"ZIP","12345"});
    if(check_dict_case(dict)){
        printf("true\n");
    }else{
        printf("false\n");
    }
    return 0;
}
