    if(txt.find(" ") != string::npos){
        vector<string> result;
        size_t pos = 0;
        string token;
        while((pos = txt.find(" ")) != string::npos){
            token = txt.substr(0, pos);
            result.push_back(token);
            txt.erase(0, pos + 1);
        }
        result.push_back(txt);
        return result;
    }
    else if(txt.find(",") != string::npos){
        vector<string> result;
        size_t pos = 0;
        string token;
        while((pos = txt.find(",")) != string::npos){
            token = txt.substr(0, pos);
            result.push_back(token);
            txt.erase(0, pos + 1);
        }
        result.push_back(txt);
        return result;
    }
    else{
        int count = 0;
        for(int i = 0; i < txt.length(); i++){
            if((int)txt[i] >= 97 && (int)txt[i] <= 122){
                if(count % 2 != 0){
                    count++;
                }
            }
        }
        vector<string> result;
        result.push_back(to_string(count));
        return result;
    }
}

int main(){
    string txt = "Hello world!";
    vector<string> result = split_words(txt);
    for(const string& s: result){
        cout << s << endl;
    }
    return 0;
}

B:
```c
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<string> split_words(string txt) {
    vector<string> result;

    // Find the first whitespace
    size_t pos = txt.find(" ");

    // If there are no whitespaces
    if (pos == string::npos) {
        // Check if there are commas
        pos = txt.find(",");

        // If there are no commas, split on lowercase letters with odd order
        if (pos == string::npos) {
            int count = 0;
            for (char c : txt) {
                if (c >= 'a' && c <= 'z' && (int)c % 2 != 0) {
                    count++;
                }
            }
            result.push_back(to_string(count));
        } else {
            // Split on commas
            while (pos != string::npos) {
                string token = txt.substr(0, pos);
                result.push_back(token);
               