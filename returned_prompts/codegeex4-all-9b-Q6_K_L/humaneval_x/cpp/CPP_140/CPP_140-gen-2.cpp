#include <iostream>
#include <string>
using namespace std;

string fix_spaces(string text){
    int count = 0;
    string result = "";
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            count++;
            if(count > 2){
                result += '-';
            } else {
                result += '_';
            }
        } else {
            count = 0;
            result += text[i];
        }
    }
    return result;
}

int main() {
    cout << fix_spaces("Example") << endl;  // "Example"
    cout << fix_spaces("Example 1") << endl;  // "Example_1"
    cout << fix_spaces(" Example 2") << endl;  // "_Example_2"
    cout << fix_spaces(" Example   3") << endl;  // "_Example-3"
    return 0;
}
B:
#include <iostream>
#include <string>
using namespace std;

string fix_spaces(string text){
    int count = 0;
    string result = "";
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            count++;
            if(count > 2){
                result += '-';
            } else {
                result += '_';
            }
        } else {
            count = 0;
            result += text[i];
        }
    }
    return result;
}

int main() {
    cout << fix_spaces("Example") << endl;  // "Example"
    cout << fix_spaces("Example 1") << endl;  // "Example_1"
    cout << fix_spaces(" Example 2") << endl;  // "_Example_2"
    cout << fix_spaces(" Example   3") << endl;  // "_Example-3"
    return 0;
}

C:
#include<stdio.h>
#include<string>
using namespace std;
string fix_spaces(string text){
    int count = 0;
    string result = "";
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            count++;
            if(count > 2){
                result += '-';
            } else {
                result += '_';
            }
        } else {
            count = 0;
            result += text[i];
        }
    }
    return result;
}

D:
#include <iostream>
#include <string>
using namespace std;

string fix_spaces(string text){
    int count