    if(dict.empty()){
        return false;
    }
    bool lower=true;
    bool upper=true;
    for(auto it=dict.begin();it!=dict.end();it++){
        if(it->first[0]>='A' && it->first[0]<='Z'){
            lower=false;
        }
        if(it->first[0]>='a' && it->first[0]<='z'){
            upper=false;
        }
        if(lower && upper){
            return false;
        }
    }
    return true;
}
int main(){
    map<string,string> dict={{ {"a","apple"}, {"b","banana"} }};
    bool ans=check_dict_case(dict);
    if(ans){
        printf("true\n");
    }else{
        printf("false\n");
    }
    return 0;
}
