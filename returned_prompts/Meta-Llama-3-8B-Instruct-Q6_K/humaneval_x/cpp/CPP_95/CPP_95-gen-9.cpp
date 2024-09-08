    if(dict.empty()) return false; 
    bool all_lower = true;
    bool all_upper = true;

    for(auto it = dict.begin(); it != dict.end(); ++it) {
        string key = it->first;
        if(!islower(key[0])) {
            all_lower = false;
        }
        if(!isupper(key[0])) {
            all_upper = false;
        }
    }
    return all_lower || all_upper;
}

int main() {
    map<string, string> dict = {{"a", "apple"}, {"b", "banana"}};
    printf("%d\n", check_dict_case(dict));  // Expected output: 1
    dict = {{"A", "banana"}, {"B", "banana"}, {"C", "banana"}};
    printf("%d\n", check_dict_case(dict));  // Expected output: 0
    dict = {{"8", "banana"}, {"a", "apple"}};
    printf("%d\n", check_dict_case(dict));  // Expected output: 0
    dict = {{"Name", "John"}, {"Age", "36"}, {"City", "Houston"}};
    printf("%d\n", check_dict_case(dict));  // Expected output: 0
    dict = {{"STATE", "NC"}, {"ZIP", "12345"} };
    printf("%d\n", check_dict_case(dict));  // Expected output: 1
    return 0;
}
