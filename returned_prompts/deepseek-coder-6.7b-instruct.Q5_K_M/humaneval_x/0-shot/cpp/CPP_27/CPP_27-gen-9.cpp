    for(int i=0; i<str.length(); i++){
        if(islower(str[i])){
            str[i] = toupper(str[i]);
        }
        else if(isupper(str[i])){
            str[i] = tolower(str[i]);
        }
    }
    return str;
}

int main(){
    string str;
    printf("Enter a string: ");
    getline(cin, str);
    printf("Flipped case string: %s", filp_case(str).c_str());
}
```

This C++ program takes a string as input and returns a new string where every lowercase character is converted to uppercase and every uppercase character is converted to lowercase. The islower() and isupper() functions are used to check if a character is lowercase or uppercase respectively. The toupper() and tolower() functions are used to convert lowercase to uppercase and uppercase to lowercase respectively. The result is a new string with the flipped case.

Test this program with "Hello". The output should be "hELLO".

This program can be compiled and run in any C++ compiler.
*/

#include <iostream>
#include <string>
#include <cctype>

std::string flip_case(std::string str) {
    for (int i = 0; i < str.length(); i++) {
        if (std::islower(str[i])) {
            str[i] = std::toupper(str[i]);
        } else if (std::isupper(str[i])) {
            str[i] = std::tolower(str[i]);
        }
    }
    return str;
}

int main() {
    std::string str;
    std::cout << "Enter a string: ";
    std::getline(std::cin, str);
    std::cout << "Flipped case string: " << flip_case(str) << std::endl;
    return 0;
}
```
This program works by iterating through each character of the string. If the character is lowercase, it is