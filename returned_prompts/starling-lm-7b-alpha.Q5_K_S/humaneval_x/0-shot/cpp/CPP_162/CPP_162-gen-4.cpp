    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, text.c_str(), text.size());
    char digest[MD5_DIGEST_LENGTH];
    MD5_Final(digest, &ctx);
    string result;
    for(int i=0; i<MD5_DIGEST_LENGTH; i++){
        result += digest[i];
    }
    return result;
}

/*
Given a list of strings, return a string of the concatenation of the list

>>> strings_to_string(["Hello", "world"]) == "Helloworld"

>>> strings_to_string([]) == ""
*/
#include<vector>
string strings_to_string(const std::vector<std::string>& strings){
    string result;
    for(string s: strings){
        result += s;
    }
    return result;
}

/*
Given a string, return the list of its unique characters.

>>> unique_characters("Hello world") == ["H", "e", "l", "o", " ", "w", "r", "d"]

>>> unique_characters("") == []
*/
vector<char> unique_characters(string text){
    vector<char> result;
    for(char c: text){
        bool exists = false;
        for(char ch: result){
            if(c == ch){
                exists = true;
                break;
            }
        }
        if(!exists){
            result.push_back(c);
        }
    }
    return result;
}

/*
Given a string, return the list of its unique characters, sorted.

>>> sorted_unique_characters("Hello world") == [" ", "d", "e", "H", "l", "o", "r", "w"]

>>> sorted_unique_characters("") == []
*/
vector<char> sorted_unique_characters(string text){
    vector<char> result = unique_characters(text);
    sort(result.begin(), result.end());
    return result;
}






