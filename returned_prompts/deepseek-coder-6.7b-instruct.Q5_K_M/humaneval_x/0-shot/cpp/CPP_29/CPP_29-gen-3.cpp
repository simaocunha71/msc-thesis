    vector<string> result;
    for(int i=0; i<strings.size(); i++){
        if(strings[i].substr(0, prefix.size()) == prefix){
            result.push_back(strings[i]);
        }
    }
    return result;
}

int main(){
    vector<string> strings = {"abc", "bcd", "cde", "vector"};
    string prefix = "a";
    vector<string> result = filter_by_prefix(strings, prefix);
    for(int i=0; i<result.size(); i++){
        printf("%s\n", result[i].c_str());
    }
    return 0;
}

*/

// TODO: Add your code here
/*
