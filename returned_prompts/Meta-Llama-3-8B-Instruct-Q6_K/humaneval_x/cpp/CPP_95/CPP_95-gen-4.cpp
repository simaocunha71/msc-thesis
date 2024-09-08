    if(dict.empty()){
        return false;
    }
    bool all_lower = true;
    bool all_upper = true;
    for(auto it = dict.begin(); it != dict.end(); ++it){
        string key = it->first;
        if(!islower(key[0])) all_lower = false;
        if(!isupper(key[0])) all_upper = false;
    }
    return all_lower || all_upper;
}

B:
    if(dict.empty()){
        return false;
    }
    bool all_lower = true;
    bool all_upper = true;
    for(auto it = dict.begin(); it != dict.end(); ++it){
        string key = it->first;
        if(!islower(key[0])) all_upper = false;
        else all_lower = false;
    }
    return all_lower || all_upper;
}

C:
    if(dict.empty()){
        return false;
    }
    bool all_lower = true;
    bool all_upper = true;
    for(auto it = dict.begin(); it != dict.end(); ++it){
        string key = it->first;
        if(isupper(key[0])) all_upper = false;
        else if(islower(key[0])) all_lower = false;
    }
    return all_lower || all_upper;
}

D:
    if(dict.empty()){
        return false;
    }
    bool all_lower = true;
    bool all_upper = true;
    for(auto it = dict.begin(); it != dict.end(); ++it){
        string key = it->first;
        if(!isalpha(key[0])) return false;
        if(isupper(key[0])) all_upper = false;
        else all_lower = false;
    }
    return all_lower || all_upper;
}

int main(){
    map<string,string> dict;
    dict["a"]="apple";
    dict["b"]="banana";
    printf("%d\n", check_dict_case(dict));
    return 0;
}
//The output should be 1 (true)
int main(){
    map<string,string> dict;
    dict["a"]="apple";
    dict["b"]="banana";
    dict["A"]="banana";
    dict["B"]="banana";
    printf("%d\n", check_dict_case(dict));
    return 0;
}
//The output should be 0 (false)
int main(){
    map<string,string> dict;
    dict["a"]="apple";
    dict["8"]="banana";
    printf("%d\n", check_dict_case(dict));
    return 0;
}
//