    if (strings.empty()){
        return NULL;
    }
    string longest = strings[0];
    for (int i = 1; i < strings.size(); i++){
        if (strings[i].length() > longest.length()){
            longest = strings[i];
        }
    }
    return longest;
}

int main(){
    vector<string> strings = {"a", "bb", "ccc"};
    printf("%s", longest(strings).c_str());
    return 0;
}

*/

/*
CORRECT CODE:
#include<iostream>
#include<vector>
#include<string>
using namespace std;

string longest(vector<string> strings){
    if (strings.empty()){
        return "";
    }
    string longest = strings[0];
    for (int i = 1; i < strings.size(); i++){
        if (strings[i].length() > longest.length()){
            longest = strings[i];
        }
    }
    return longest;
}

int main(){
    vector<string> strings = {"a", "bb", "ccc"};
    cout << longest(strings) << endl;
    return 0;
}
*/

/*
CORRECT CODE:
#include<vector>
#include<string>
using namespace std;

string longest(vector<string> strings){
    if (strings.empty()){
        return "";
    }
    string longest = strings[0];
    for (string s: strings){
        if (s.length() > longest.length()){
            longest = s;
        }
    }
    return longest;
}
*/

CORRECT CODE:
#include<vector>
#include<string>
using namespace std;

string longest(vector<string> strings){
    if (strings.empty()){
        return "";
    }
    string longest = strings[0];
    for (string s: strings){
        if (s.length() > longest.length()){
            longest = s;
        }
    }
    return longest;
}

//