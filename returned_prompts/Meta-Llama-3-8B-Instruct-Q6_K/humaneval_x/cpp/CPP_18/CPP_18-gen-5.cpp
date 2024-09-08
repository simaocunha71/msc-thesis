    int count = 0; 
    int str_len = str.length();
    int substring_len = substring.length();
    for(int i = 0; i <= str_len - substring_len; i++){
        if(str.substr(i, substring_len) == substring){
            count++;
        }
    }
    return count;
}  



C:
#include <stdio.h>
#include <string.h>

int how_many_times(char *str, char *substring) {
    int count = 0;
    int str_len = strlen(str);
    int substring_len = strlen(substring);
    for(int i = 0; i <= str_len - substring_len; i++){
        if(strncmp(str+i, substring, substring_len) == 0){
            count++;
        }
    }
    return count;
}

int main() {
    printf("%d\n", how_many_times("aaa", "a"));
    printf("%d\n", how_many_times("aaaa", "aa"));
    return 0;
}

Output:
3
3
*/



C++ (Using Regular Expressions):
#include <iostream>
#include <regex>

int how_many_times(std::string str, std::string substring) {
    std::regex pattern(substring);
    int count = std::count_if(str.begin(), str.end(), std::regex_match);
    return count;
}

int main() {
    std::cout << how_many_times("aaa", "a") << std::endl;
    std::cout << how_many_times("aaaa", "aa") << std::endl;
    return 0;
}  



C++ (Using Loop):
#include <iostream>
#include <string>

int how_many_times(std::string str, std::string substring) {
    int count = 0;
    int str_len = str.length();
    int substring_len = substring.length();
    for(int i = 0; i <= str_len - substring_len; i++){
        if(str.substr(i, substring_len) == substring){
            count++;
        }
    }
    return count;
}

int main() {
    std::cout << how_many_times("aaa", "a") << std::endl;
    std::cout << how_many_times("aaaa", "aa") << std::endl;
    return 0;
}

Output:
3
3
*/



Note: The function `how_many_times` counts the number of times a given substring appears in the original string. The `main` function tests the function with the strings "aaa" and