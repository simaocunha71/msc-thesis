    string word = "", result = "";
    int i, j, len;
    bool is_prime;

    len = sentence.length();

    for(i=0; i<len; i++){

        // extract words from sentence
        if(sentence[i] != ' '){
            word = word + sentence[i];
        }
        else{
            // check if word length is a prime number
            is_prime = true;
            if(word.length() == 1 || word.length() == 0){
                is_prime = false;
            }
            else{
                for(j=2; j*j<=word.length(); j++){
                    if(word.length() % j == 0){
                        is_prime = false;
                        break;
                    }
                }
            }

            // if word length is a prime number then add it to result
            if(is_prime){
                result = result + word + " ";
            }

            word = "";
        }
    }

    // check for last word in sentence
    if(word.length() > 0){
        is_prime = true;
        if(word.length() == 1 || word.length() == 0){
            is_prime = false;
        }
        else{
            for(j=2; j*j<=word.length(); j++){
                if(word.length() % j == 0){
                    is_prime = false;
                    break;
                }
            }
        }

        if(is_prime){
            result = result + word;
        }
    }

    return result;
}

int main() {
    string sentence;
    printf("Enter a sentence: ");
    getline(cin, sentence);
    printf("Result: %s\n", words_in_sentence(sentence).c_str());
    return 0;
}
*/






/*
// C++ program to check if a number is prime
#include<bits/stdc++.h>
using namespace std;

bool isPrime(int n) {
    if (n <= 1)
       