    string result;
    for(int i=word.length()-1;i>=0;i--){
        if(isalpha(word[i]) && !isupper(word[i]) && word[i]!='A' && word[i]!='E' && word[i]!='I' && word[i]!='O' && word[i]!='U'){
            for(int j=i-1;j>=0;j--){
                if(isalpha(word[j]) && (isupper(word[j]) || (word[j]=='A' || word[j]=='E' || word[j]=='I' || word[j]=='O' || word[j]=='U'))){
                    result = word.substr(j,i-j);
                    return result;
                }
            }
        }
    }
    return result;
}
int main(){
    printf("%s\n",get_closest_vowel("yogurt").c_str());  // output: "u"
    printf("%s\n",get_closest_vowel("FULL").c_str());  // output: "U"
    printf("%s\n",get_closest_vowel("quick").c_str());  // output: ""
    printf("%s\n",get_closest_vowel("ab").c_str());  // output: ""
    return 0;
}

Solution:
The solution is a simple loop that goes through the word from right to left. For each character, it checks if it is a consonant. If it is, it then checks the characters to its left to find the first vowel. If it finds a vowel, it returns the substring from the vowel to the current character.

Here is the C++ code for the solution:

```cpp
#include <iostream>
#include <string>
using namespace std;

string get_closest_vowel(string word) {
    for (int i = word.length() - 1; i >= 0; i--) {
        if (!isalpha(word[i])) continue;
        if (isupper(word[i]) || (word[i] == 'A' || word[i] == 'E' || word[i] == 'I' || word[i] == 'O' || word[i] == 'U')) {
            for (int j = i - 1; j >= 0; j--) {
                if (!isalpha(word[j])) continue;
                if (isupper(word[j]) || (word[j] == 'A' || word[j] == 'E' || word[j] == 'I' || word[j] == 'O' || word[j] == 'U')) {
                   