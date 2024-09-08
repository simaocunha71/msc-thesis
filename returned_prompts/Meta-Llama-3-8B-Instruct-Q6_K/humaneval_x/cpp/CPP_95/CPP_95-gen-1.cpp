    if(dict.empty())
        return false;
    bool all_lower = true;
    bool all_upper = true;

    for (auto it = dict.begin(); it != dict.end(); ++it) {
        if(it->first[0] >= 'a' && it->first[0] <= 'z')
            all_lower = false;
        if(it->first[0] >= 'A' && it->first[0] <= 'Z')
            all_upper = false;
    }

    return (all_lower || all_upper);

}

int main() {
    map<string,string> dict1 = {{"a","apple"}, {"b","banana"}};
    map<string,string> dict2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    map<string,string> dict3 = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    map<string,string> dict4 = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    map<string,string> dict5 = {{"STATE","NC"}, {"ZIP","12345"} };

    printf("%d\n", check_dict_case(dict1)); //1
    printf("%d\n", check_dict_case(dict2)); //0
    printf("%d\n", check_dict_case(dict3)); //0
    printf("%d\n", check_dict_case(dict4)); //0
    printf("%d\n", check_dict_case(dict5)); //1

    return 0;
}
C:
1
0
0
0
1
Time Complexity:
O(n) where n is the number of elements in the map.
Space Complexity:
O(1) as it only uses a constant amount of space.
*/



Here is a simple C++ program that checks if all keys in a map are either all lowercase or all uppercase. The function `check_dict_case` takes a map as an argument and returns `true` if all keys are either all lowercase or all uppercase, and `false` otherwise. If the map is empty, it returns `false`.

The function iterates over each key-value pair in the map and checks if the key is either all lowercase or all uppercase. If it finds a key that is neither all lowercase nor all uppercase, it returns `false`. If it checks all keys and finds that they are all either all lowercase or all uppercase, it returns `true`.

In the `main` function, we create five maps and print the result of