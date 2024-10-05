    if(dict.empty()) return false;
    map<string,string>::iterator it;
    bool is_lower = true;
    bool is_upper = true;
    for(it = dict.begin(); it != dict.end(); it++){
        if(!islower(it->first[0]) && !isupper(it->first[0])){
            is_lower = false;
        }
        if(!islower(it->first[0]) && !isupper(it->first[0])){
            is_upper = false;
        }
    }
    if(is_lower || is_upper) return true;
    else return false;
}

int main(){
    map<string,string> dict1 = {{"a","apple"}, {"b","banana"}};
    map<string,string> dict2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    map<string,string> dict3 = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    map<string,string> dict4 = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    map<string,string> dict5 = {{"STATE","NC"}, {"ZIP","12345"} };
    bool ret1 = check_dict_case(dict1);
    bool ret2 = check_dict_case(dict2);
    bool ret3 = check_dict_case(dict3);
    bool ret4 = check_dict_case(dict4);
    bool ret5 = check_dict_case(dict5);
    printf("%d\n", ret1);
    printf("%d\n", ret2);
    printf("%d\n", ret3);
    printf("%d\n", ret4);
    printf("%d\n", ret5);
}
