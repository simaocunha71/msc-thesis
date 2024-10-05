vector<string> result;
for(auto &str: lst){
    if(str.size()%2 == 0){
        result.push_back(str);
    }
}
sort(result.begin(), result.end());
return result;
}

int main() {
    vector<string> test1 = {"aa", "a", "aaa"};
    vector<string> test2 = {"ab", "a", "aaa", "cd"};
    vector<string> result = sorted_list_sum(test2);
    for(auto &str: result){
        printf("%s ", str.c_str());
    }
    return 0;
}

