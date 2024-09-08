    // check if string contains any whitespace
    if(txt.find(' ') != string::npos){
        // if yes, split on whitespace
        vector<string> result;
        size_t pos = 0;
        while ((pos = txt.find(' ')) != string::npos) {
            result.push_back(txt.substr(0, pos));
            txt.erase(0, pos + 1);
        }
        result.push_back(txt);
        return result;
    }
    else{
        // if no whitespace, check if string contains commas
        if(txt.find(',') != string::npos){
            // if yes, split on commas
            vector<string> result;
            size_t pos = 0;
            while ((pos = txt.find(',')) != string::npos) {
                result.push_back(txt.substr(0, pos));
                txt.erase(0, pos + 1);
            }
            result.push_back(txt);
            return result;
        }
        else{
            // if no commas, return a vector with one element, the number of lower-case letters with odd order in the alphabet
            int count = 0;
            for(int i = 0; i < txt.length(); i++){
                char c = tolower(txt[i]);
                if(c >= 'a' && c <= 'z' && (c - 'a') % 2 != 0)
                    count++;
            }
            vector<string> result;
            result.push_back(to_string(count));
            return result;
        }
    }
}

int main() {
    string text = "Hello world!";
    vector<string> result = split_words(text);
    for(auto s : result)
        printf("%s\n", s.c_str());
    return 0;
}
Output:
Hello
world!

Program Description:
The program defines a function `split_words` that takes a string as input and returns a vector of strings. The function splits the input string into words based on whitespace and commas. If the input string contains no whitespace or commas, it counts the number of lower-case letters with odd order in the alphabet and returns a vector with one element containing this count.

In the `main` function, the program tests the `split_words` function with the input string "Hello world!" and prints the resulting vector of strings.

Note: The program uses the `tolower` function from the `<cctype>` library to convert uppercase letters to lowercase. It also uses the `find` function from the `<string>` library to search for whitespace and commas in the