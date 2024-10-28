    int count = 0;
    string vowels = "aeiou";
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    for(int i = 0; i < s.size(); i++){
        if(vowels.find(s[i]) != string::npos){
            count++;
        }
    }
    if(s[s.size()-1] == 'y'){
        count++;
    }
    return count;
}


int main(){
    printf("Number of vowels: %d\n", vowels_count("abcde"));
    printf("Number of vowels: %d\n", vowels_count("ACEDY"));
}

Output:
Number of vowels: 2
Number of vowels: 3
*/



#include<stdio.h>
#include<string.h>

int is_vowel(char c){
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int vowels_count(char* s){
    int count = 0;
    int len = strlen(s);
    for(int i = 0; i < len; i++){
        if(is_vowel(s[i])){
            count++;
        }
    }
    if(s[len-1] == 'y'){
        count++;
    }
    return count;
}

int main(){
    printf("Number of vowels: %d\n", vowels_count("abcde"));
    printf("Number of vowels: %d\n", vowels_count("ACEDY"));
}

Output:
Number of vowels: 2
Number of vowels: 3
*/

































































