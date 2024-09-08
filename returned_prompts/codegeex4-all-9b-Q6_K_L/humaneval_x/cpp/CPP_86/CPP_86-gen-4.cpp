#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string anti_shuffle(string s){
    string result = "";
    string word = "";
    for (char c : s){
        if (c == ' '){
            sort(word.begin(), word.end());
            result += word + ' ';
            word = "";
        } else {
            word += c;
        }
    }
    sort(word.begin(), word.end());
    result += word;
    return result;
}

B:
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string anti_shuffle(string s){
    string result = "";
    string word = "";
    for (char c : s){
        if (c == ' '){
            sort(word.begin(), word.end());
            result += word + ' ';
            word = "";
        } else {
            word += c;
        }
    }
    sort(word.begin(), word.end());
    result += word;
    return result;
}

C:
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string anti_shuffle(string s){
    string result = "";
    string word = "";
    for (char c : s){
        if (c == ' '){
            sort(word.begin(), word.end());
            result += word + ' ';
            word = "";
        } else {
            word += c;
        }
    }
    sort(word.begin(), word.end());
    result += word;
    return result;
}

D:
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string anti_shuffle(string s){
    string result = "";
    string word = "";
    for (char c : s){
        if (c == ' '){
            sort(word.begin(), word.end());
            result += word + ' ';
            word = "";
        } else {
            word += c;
        }
    }
    sort(word.begin(), word.end());
    result += word;
    return result;
}

E:
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string anti_shuffle(string s){
    string result = "";
    string word = "";
    for (char c : s){
        if (c == ' '){
            sort(word.begin(), word.end());
            result += word + ' ';
            word = "";
        } else {
            word += c;
        }
    }
    sort(word.begin(), word.end());
    result += word;
    return result;
}

F:
#include <iostream>
#include <algorithm>
#include <string>
