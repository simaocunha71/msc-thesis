#include <string>
#include <map>
using namespace std;

bool check_dict_case(map<string,string> dict) {
    if (dict.empty()) return false;

    int c = 0; // count of lower case or upper case
    for (const auto& kv : dict) {
        if (islower(kv.first[0])) {
            ++c;
        }
        else if (isupper(kv.first[0])) {
            --c;
        }
        else {
            return false;
        }
    }

    return c == 0;
}

void test() {
    map<string,string> dict1 = {{"a","apple"}, {"b","banana"}};
    map<string,string> dict2 = {{"a","apple"}, {"A","banana"}, {"B","banana"}};
    map<string,string> dict3 = {{"a","apple"}, {"8","banana"}, {"a","apple"}};
    map<string,string> dict4 = {{"Name","John"}, {"Age","36"}, {"City","Houston"}};
    map<string,string> dict5 = {{"STATE","NC"}, {"ZIP","12345"} };
    printf("%d\n", check_dict_case(dict1));
    printf("%d\n", check_dict_case(dict2));
    printf("%d\n", check_dict_case(dict3));
    printf("%d\n", check_dict_case(dict4));
    printf("%d\n", check_dict_case(dict5));
}

int main() {
    test();
    return 0;
}