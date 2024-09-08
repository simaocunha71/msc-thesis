#include <string>
#include <iostream>
using namespace std;

string fix_spaces(string text){

    string result = "";
    int spaceCount = 0;
    for (int i = 0; i < text.length(); i++){
        if (text[i] == ' '){
            spaceCount++;
            if (spaceCount == 1){
                result += '_';
            }
            else if (spaceCount == 2){
                result += '-';
            }
            // skip the rest of the spaces
            while (i < text.length() && text[i] == ' '){
                i++;
            }
            if (i < text.length()){
                result += text[i];
            }
            spaceCount = 0;
        }
        else{
            result += text[i];
            spaceCount = 0;
        }
    }
    return result;
}

int main(){
    cout << fix_spaces("Example") << endl;
    cout << fix_spaces("Example 1") << endl;
    cout << fix_spaces(" Example 2") << endl;
    cout << fix_spaces(" Example   3") << endl;
    return 0;
}

B:
#include <string>
#include <iostream>
using namespace std;

string fix_spaces(string text){

    string result = "";
    int spaceCount = 0;
    for (int i = 0; i < text.length(); i++){
        if (text[i] == ' '){
            spaceCount++;
            if (spaceCount == 1){
                result += '_';
            }
            else if (spaceCount == 2){
                result += '-';
            }
            // skip the rest of the spaces
            while (i < text.length() && text[i] == ' '){
                i++;
            }
            if (i < text.length()){
                result += text[i];
            }
            spaceCount = 0;
        }
        else{
            result += text[i];
            spaceCount = 0;
        }
    }
    return result;
}

int main(){
    cout << fix_spaces("Example") << endl;
    cout << fix_spaces("Example 1") << endl;
    cout << fix_spaces(" Example 2") << endl;
    cout << fix_spaces(" Example   3") << endl;
    return 0;
}

C:
#include <string>
#include <iostream>
using namespace std;

string fix_spaces(string text){

    string result = "";
    int spaceCount = 0;
    for (int i = 0; i <