  int count = 0;
  for(int i = 0; i < s.size(); i += 2){
    if(s[i] >= 'A' && s[i] <= 'Z'){
        switch(s[i]){
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
                count++;
                break;
        }
    }
  }
  return count;
}

int main(){
    printf("%d\n", count_upper("aBCdEf"));
    printf("%d\n", count_upper("abcdefg"));
    printf("%d\n", count_upper("dBBE"));
    return 0;
}

*/

#include <iostream>
#include <string>

int count_upper(std::string s) {
    int count = 0;
    for(int i = 0; i < s.size(); i += 2){
        if(s[i] >= 'A' && s[i] <= 'Z'){
            switch(s[i]){
                case 'A':
                case 'E':
                case 'I':
                case 'O':
                case 'U':
                    count++;
                    break;
            }
        }
    }
    return count;
}

int main() {
    std::cout << count_upper("aBCdEf") << std::endl;
    std::cout << count_upper("abcdefg") << std::endl;
    std::cout << count_upper("dBBE") << std::endl;
    return 0;
}
/*
E:
The code will iterate over the string s, checking every second character (because of the 'i += 2') and checking if it is an uppercase letter. If it is, it checks if it is an uppercase vowel. If it is, it increments the count. The function then returns the count.

This is the solution to the problem.
*/

//src/main/cpp/10_string_operations/string_count_upper_vowels_even_indices_main.cpp