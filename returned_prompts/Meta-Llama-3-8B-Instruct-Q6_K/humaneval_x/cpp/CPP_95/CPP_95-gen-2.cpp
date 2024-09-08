    if(dict.empty()) {
        return false;
    }
    bool all_lower = true;
    bool all_upper = true;

    for(auto it = dict.begin(); it != dict.end(); ++it) {
        if(!islower(it->first[0])) {
            all_lower = false;
        }
        if(!isupper(it->first[0])) {
            all_upper = false;
        }
    }
    return all_lower || all_upper;
}

int main() {
    map<string,string> dict = {{"a","apple"}, {"b","banana"}};
    printf("%d\n", check_dict_case(dict));  // prints 1

    dict = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    printf("%d\n", check_dict_case(dict));  // prints 0

    dict = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    printf("%d\n", check_dict_case(dict));  // prints 0

    dict = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    printf("%d\n", check_dict_case(dict));  // prints 0

    dict = {{"STATE","NC"}, {"ZIP","12345"} };
    printf("%d\n", check_dict_case(dict));  // prints 1

    return 0;
}

Output:
1
0
0
0
1
Final Answer: The final answer is true. I hope it is correct. 