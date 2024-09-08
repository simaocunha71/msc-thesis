    if(dict.empty()) // check if the map is empty
        return false;
    bool all_upper=true;
    bool all_lower=true;
    for(auto it = dict.begin(); it != dict.end(); it++) {
        if(it->first[0] >= 'a' && it->first[0] <= 'z') {
            all_upper = false;
        }
        if(it->first[0] >= 'A' && it->first[0] <= 'Z') {
            all_lower = false;
        }
    }
    return all_upper || all_lower;
}

int main() {
    map<string, string> dict1 = {{"a","apple"}, {"b","banana"}};
    map<string, string> dict2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    map<string, string> dict3 = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    map<string, string> dict4 = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    map<string, string> dict5 = {{"STATE","NC"}, {"ZIP","12345"} };

    cout << check_dict_case(dict1) << endl; // should return 1
    cout << check_dict_case(dict2) << endl; // should return 0
    cout << check_dict_case(dict3) << endl; // should return 0
    cout << check_dict_case(dict4) << endl; // should return 0
    cout << check_dict_case(dict5) << endl; // should return 1

    return 0;
}

B:
    bool check_map_case(map<string,string> dict) {
        if(dict.empty()) return false;
        bool all_upper=true;
        bool all_lower=true;
        for(auto it = dict.begin(); it != dict.end(); it++) {
            if(it->first[0] >= 'a' && it->first[0] <= 'z') all_lower=false;
            if(it->first[0] >= 'A' && it->first[0] <= 'Z') all_upper=false;
        }
        return all_upper || all_lower;
    }

    int main() {
        map<string, string> dict1 = {{"a","apple"}, {"b","banana"}};
        map<string, string> dict2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
        map<string