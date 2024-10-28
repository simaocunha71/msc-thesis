    int count = 0;
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for(int i=0; i<s.length(); i++){
        if(s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='o'||s[i]=='u'){
            count++;
        }
    }
    if(s[s.length()-1] == 'y'){
        count++;
    }
    return count;
}

int main(){
    printf("%d\n", vowels_count("abcde"));
    printf("%d\n", vowels_count("ACEDY"));
    return 0;
}
```
This C++ program is a solution to the problem. It counts the number of vowels in a given string and also checks if 'y' is the last character in the string, if yes then it counts 'y' as a vowel.

First, the program converts the whole string to lower case to handle cases where uppercase letters are passed as input. Then, it checks each character in the string if it is a vowel or not. If it is, it increments the count. If the last character in the string is 'y', it also increments the count. Finally, it returns the count.

This program will output:

```
2
3
```
for the input "abcde" and "ACEDY" respectively.

Please note that this program only works for English alphabets. For strings in other languages, a different approach might be required.
*/

#include <stdio.h>
#include <string.h>

int vowels_count(char *s) {
    int count = 0;
    for (int i = 0; i < strlen(s); i++) {
        char c = tolower(s[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }
    if (s[strlen(s) - 1] == 'y')