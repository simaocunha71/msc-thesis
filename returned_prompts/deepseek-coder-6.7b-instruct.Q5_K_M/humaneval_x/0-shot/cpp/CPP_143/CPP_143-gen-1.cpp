    
}

int main(){
    string sentence;
    getline(cin, sentence);
    string output = words_in_sentence(sentence);
    cout << output << endl;
    return 0;
}
*/

#include<string>
#include<vector>
using namespace std;

bool isPrime(int n) {
    if(n <= 1) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;
    for(int i = 3; i * i <= n; i += 2) {
        if(n % i == 0) return false;
    }
    return true;
}

string words_in_sentence(string sentence){
    string word = "", ans = "";
    for(int i = 0; i < sentence.size(); i++){
        if(sentence[i] == ' '){
            if(isPrime(word.size())){
                ans += word + ' ';
            }
            word = "";
        } else {
            word += sentence[i];
        }
    }
    if(isPrime(word.size())){
        ans += word;
    }
    return ans;
}

//tests/test_words_in_sentence.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "words_in_sentence.cpp"

TEST_CASE("Words in sentence") {
    REQUIRE(words_in_sentence("This is a test") == "is ");
    REQUIRE(words_in_sentence("lets go for swimming") == "go for ");
    REQUIRE(words_in_sentence("The quick brown fox jumps over the lazy dog") == "quick brown fox jumps over ");
    REQUIRE(words_in_sentence("") == "");
}/*
