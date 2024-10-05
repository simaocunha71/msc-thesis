    vector<string> words;
    if(txt.find(' ') != string::npos){
        string word;
        for(char c : txt){
            if(c == ' '){
                words.push_back(word);
                word = "";
            }
            else{
                word += c;
            }
        }
        words.push_back(word);
    }
    else if(txt.find(',') != string::npos){
        string word;
        for(char c : txt){
            if(c == ','){
                words.push_back(word);
                word = "";
            }
            else{
                word += c;
            }
        }
        words.push_back(word);
    }
    else{
        int count = 0;
        for(char c : txt){
            if(c >= 'a' && c <= 'z' && (c - 'a') % 2 == 1){
                count++;
            }
        }
        words.push_back(to_string(count));
    }

    return words;
}

*/

// Test the function
int main(){
    vector<string> words = split_words("Hello world!");
    for(string word : words){
        printf("%s ", word.c_str());
    }
    printf("\n");

    words = split_words("Hello,world!");
    for(string word : words){
        printf("%s ", word.c_str());
    }
    printf("\n");

    words = split_words("abcdef");
    for(string word : words){
        printf("%s ", word.c_str());
    }
    printf("\n");

    return 0;
}

*/

// Expected Output:
// Hello world
// Hello world
// 3
// Process returned 0 (0x0)   execution time : 0.003 s
// Press any key to continue.

/*
This program splits a string into words based on either whitespace or commas. If neither of these characters are present, it counts the number of lower-case letters