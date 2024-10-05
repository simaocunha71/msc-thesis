    vector<string> words;
    string word = "";
    for (int i = 0; i < s.length(); i++){
        if (s[i] == ',' || s[i] == ' '){
            if (word != ""){
                words.push_back(word);
                word = "";
            }
        }
        else{
            word += s[i];
        }
    }
    if (word != ""){
        words.push_back(word);
    }
    return words;
}

int main(){
    vector<string> words = words_string("Hi, my name is John");
    for(int i = 0; i < words.size(); i++){
        printf("%s ", words[i].c_str());
    }
    return 0;
}

/*
In this code, we first create an empty vector of strings called words. We then
iterate over the input string s. If we encounter a comma or space, we add the
current word to the vector if it is not empty, and reset the word to an empty
string. If we encounter any other character, we add it to the current word.

Finally, we add the last word to the vector if it is not empty, and return the
vector. The main function then prints out the words in the vector.
*/



*/

//tests/01_words_string.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "../question/01_words_string.cpp"

TEST_CASE("Words string function") {
    REQUIRE(words_string("Hi, my name is John") == vector<string>({"Hi", "my", "name", "is", "John"}));
    REQUIRE(words_string("One, two, three, four, five, six") == vector<string>({"One", "two", "three", "four", "five", "six"}));
    REQUIRE(words_string("") == vector<string>({}));
    REQUIRE(words