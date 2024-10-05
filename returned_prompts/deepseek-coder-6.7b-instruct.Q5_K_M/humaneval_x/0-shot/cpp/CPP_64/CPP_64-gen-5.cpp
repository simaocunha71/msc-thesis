    int cnt=0;
    string vowels = "aeiou";
    transform(s.begin(),s.end(),s.begin(), ::tolower);
    for(int i=0; i<s.length(); i++){
        if(vowels.find(s[i]) != string::npos){
            cnt++;
        }
    }
    if(s[s.length()-1] == 'y'){
        cnt++;
    }
    return cnt;
}

int main(){
    printf("%d\n",vowels_count("abcde"));
    printf("%d\n",vowels_count("ACEDY"));
    return 0;
}

This program works by creating a string of vowels and then iterating through each character in the input string. If the character is found in the string of vowels, it increments a counter. The final count of the vowels is then returned.

If the last character of the string is 'y' (or 'Y'), it is also counted as a vowel.

Note: The function transform is used to convert the input string to lower case. This is done because the problem statement does not differentiate between uppercase and lowercase vowels.
*/

#include <iostream>
#include <string>
#include <algorithm>

int vowels_count(std::string s) {
    int count = 0;
    std::string vowels = "aeiou";
    std::transform(s.begin(), s.end(), s.begin(), ::tolower);
    for (char c : s) {
        if (vowels.find(c) != std::string::npos) {
            count++;
        }
    }
    if (s[s.length()-1] == 'y') {
        count++;
    }
    return count;
}

int main() {
    std::cout << vowels_count("abcde") << std::endl;
    std::cout << vowels_count("ACEDY") << std::endl;
    return 0;
}
```
This program should output:
```