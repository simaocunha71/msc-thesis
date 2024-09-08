    string result = "";
    int i = 0;
    while(i < sentence.length()){
        string word = "";
        while(i < sentence.length() && sentence[i] != ' '){
            word += sentence[i];
            i++;
        }
        if(i < sentence.length()) i++; // skip the space
        if(prime(word.length())){
            result += word + " ";
        }
    }
    return result.substr(0, result.length()-1);

}
bool prime(int n){
    if(n <= 1) return false;
    for(int i = 2; i*i <= n; i++){
        if(n%i == 0) return false;
    }
    return true;
}
int main(){
    string sentence = "This is a test";
    printf("%s\n", words_in_sentence(sentence).c_str());
    return 0;
}

Solution:
The problem can be solved by iterating through the sentence word by word, checking the length of each word, and if it's a prime number, adding it to the result string.

Here is the code:
```c
#include<stdio.h>
#include<string>
using namespace std;
string words_in_sentence(string sentence){
    string result = "";
    int i = 0;
    while(i < sentence.length()){
        string word = "";
        while(i < sentence.length() && sentence[i] != ' '){
            word += sentence[i];
            i++;
        }
        if(i < sentence.length()) i++; // skip the space
        if(prime(word.length())){
            result += word + " ";
        }
    }
    return result.substr(0, result.length()-1);
}

bool prime(int n){
    if(n <= 1) return false;
    for(int i = 2; i*i <= n; i++){
        if(n%i == 0) return false;
    }
    return true;
}

int main(){
    string sentence = "This is a test";
    printf("%s\n", words_in_sentence(sentence).c_str());
    return 0;
}
```
The code defines a function `words_in_sentence` that takes a string `sentence` as input and returns a string containing the words from the original sentence whose lengths are prime numbers.

The function iterates through the sentence word by word, checking the length of each word using the `prime` function. If the length is prime, the word is added to the result string. The function returns the result string after removing the trailing space.

The `prime` function checks if