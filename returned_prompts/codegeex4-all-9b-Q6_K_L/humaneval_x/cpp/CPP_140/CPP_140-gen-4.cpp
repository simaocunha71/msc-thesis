#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string fix_spaces(string text){
    string res;
    for(int i = 0; i < text.size(); ++i) {
        if(text[i] == ' '){
            int j = i+1;
            while(j < text.size() && text[j] == ' '){
                ++j;
            }
            if(j-i > 2) {
                res += '-';
            } else {
                res += '_';
            }
            i = j-1;
        } else {
            res += text[i];
        }
    }
    return res;
}

int main(){
    string s = "Example   3";
    string res = fix_spaces(s);
    cout << res << endl;
    return 0;
}
B:
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string fix_spaces(string text){
    string res;
    for(int i = 0; i < text.size(); ++i) {
        if(text[i] == ' '){
            int j = i+1;
            while(j < text.size() && text[j] == ' '){
                ++j;
            }
            if(j-i > 2) {
                res += '-';
            } else {
                res += '_';
            }
            i = j-1;
        } else {
            res += text[i];
        }
    }
    return res;
}

int main(){
    string s = "Example   3";
    string res = fix_spaces(s);
    cout << res << endl;
    return 0;
}

C:
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string fix_spaces(string text){
    string res;
    for(int i = 0; i < text.size(); ++i) {
        if(text[i] == ' '){
            int j = i+1;
            while(j < text.size() && text[j] == ' '){
                ++j;
            }
            if(j-i > 2) {
                res += '-';
            } else {
                res += '_';
            }
            i = j-1;
        } else {
            res += text[i];
        }
    }
    return res;
}

int main(){
    string s = "Example   3";
    string res = fix_spaces(s);
    cout << res << endl;
    return 0;
}

D:
#include <iostream>
#include <string>
#include <algorithm