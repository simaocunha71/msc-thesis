    if(dict.empty())return false;
    bool is_upper = true;
    bool is_lower = true;
    for(auto it = dict.begin(); it != dict.end(); ++it){
        if(isupper(it->first[0])){
            is_lower = false;
        }
        else if(islower(it->first[0])){
            is_upper = false;
        }
        else{
            return false;
        }
    }
    return is_upper || is_lower;
}

int main()
{
    map<string, string> m1 = {{"a","apple"}, {"b","banana"}};
    map<string, string> m2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    map<string, string> m3 = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    map<string, string> m4 = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    map<string, string> m5 = {{"STATE","NC"}, {"ZIP","12345"} };
    printf("%d\n",check_dict_case(m1)); //should print 1
    printf("%d\n",check_dict_case(m2)); //should print 0
    printf("%d\n",check_dict_case(m3)); //should print 0
    printf("%d\n",check_dict_case(m4)); //should print 0
    printf("%d\n",check_dict_case(m5)); //should print 1
    return 0;
}
B:
    The C++ program checks if all keys in a map are either in lower case or in upper case. If the map is empty, it returns false. Otherwise, it iterates over the map's elements and checks if all keys start with either a lower case or an upper case letter. If it finds a key that does not match this condition, it immediately returns false. If it has checked all keys and none of them do not match the condition, it returns true. The function is declared as bool check_dict_case(map<string, string> dict). The main function tests this function with five different maps and prints the result. The output of the program should be 1 for the first, third, and fifth map, and 0 for the second and fourth map. This is because the first, third, and fifth maps have all keys in either lower case or upper case, while the second and fourth maps do not. The fourth map has a key with