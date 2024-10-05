    if(dict.size()==0)
        return false;

    bool is_lower=true;
    bool is_upper=true;

    for(auto x:dict){
        if(!isupper(x.first[0])){
            is_upper=false;
        }
        if(!islower(x.first[0])){
            is_lower=false;
        }
        if(is_lower && is_upper)
            break;
    }

    if(is_lower || is_upper)
        return true;
    return false;
}

int main(){
    map<string,string> test1;
    test1.insert(pair<string,string>("a","apple"));
    test1.insert(pair<string,string>("b","banana"));
    if(check_dict_case(test1)==true)
        printf("true\n");
    else
        printf("false\n");

    map<string,string> test2;
    test2.insert(pair<string,string>("a","apple"));
    test2.insert(pair<string,string>("A","banana"));
    test2.insert(pair<string,string>("B","banana"));
    if(check_dict_case(test2)==false)
        printf("true\n");
    else
        printf("false\n");

    map<string,string> test3;
    test3.insert(pair<string,string>("a","apple"));
    test3.insert(pair<string,string>("A","banana"));
    test3.insert(pair<string,string>("8","banana"));
    test3.insert(pair<string,string>("a","apple"));
    if(check_dict_case(test3)==false)
        printf("true\n");
    else
        printf("false\n");

    map<string,string> test4;
    test4.insert(pair<string,string>("Name","John"));
    test4.insert(pair<string,string>("Age","36"));
    test4.insert(pair<string,string>