    if(dict.empty()){
        return false;
    }
    bool lower_case = true, upper_case = true;
    for(auto const &pair: dict){
        for(auto const &c: pair.first){
            if(islower(c)==0){
                lower_case = false;
            }
            if(isupper(c)==0){
                upper_case = false;
            }
        }
    }
    if(lower_case || upper_case){
        return true;
    }
    return false;
}

int main() {
    map<string,string> m1 = {{"a","apple"}, {"b","banana"}};
    printf("%d\n", check_dict_case(m1));
    map<string,string> m2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    printf("%d\n", check_dict_case(m2));
    map<string,string> m3 = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    printf("%d\n", check_dict_case(m3));
    map<string,string> m4 = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    printf("%d\n", check_dict_case(m4));
    map<string,string> m5 = {{"STATE","NC"}, {"ZIP","12345"}};
    printf("%d\n", check_dict_case(m5));
    return 0;
}

This solution will work for the given problem, but it's not optimal. It traverses the map twice, which makes it O(2n), which can be simplified to O(n). Also, it checks for both upper and lower case which is not necessary.

A more efficient solution will be to traverse the map once and check for both upper and lower case at the same time. This will make it O(n).

Here is the more efficient solution:

bool check_dict_case(map<string,string> dict){
    if(dict.empty()){
        return