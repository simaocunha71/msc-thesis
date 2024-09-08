    vector<string> result;
    for(int i=1; i<=str.length(); i++){
        result.push_back(str.substr(0, i));
    }
    return result;
}

int main(){
    string s = "abc";
    vector<string> prefixes = all_prefixes(s);
    for(auto prefix : prefixes){
        printf("%s\n", prefix.c_str());
    }
    return 0;
}
