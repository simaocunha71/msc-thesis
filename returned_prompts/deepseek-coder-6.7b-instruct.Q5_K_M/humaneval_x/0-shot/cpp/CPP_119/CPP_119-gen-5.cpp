    string first = lst[0], second = lst[1];
    int count = 0;
    for(int i = 0; i < first.size(); i++){
        if(first[i] == '(') count++;
        else if(first[i] == ')') count--;
        if(count < 0) return "No";
    }
    for(int i = 0; i < second.size(); i++){
        if(second[i] == '(') count++;
        else if(second[i] == ')') count--;
        if(count < 0) return "No";
    }
    if(count == 0) return "Yes";
    else return "No";
}

int main(){
    vector<string> lst = {"()(", ")"};
    printf("%s\n", match_parens(lst).c_str());
    return 0;
}

*/

//C++/MatchParens/main.cpp
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

string match_parens(vector<string> lst){
    string first = lst[0], second = lst[1];
    int count = 0;
    for(int i = 0; i < first.size(); i++){
        if(first[i] == '(') count++;
        else if(first[i] == ')') count--;
        if(count < 0) return "No";
    }
    for(int i = 0; i < second.size(); i++){
        if(second[i] == '(') count++;
        else if(second[i] == ')') count--;
        if(count < 0) return "No";
    }
    if(count == 0) return "Yes";
    else return "No";
}

int main(){
    vector<string> lst = {"()(", ")"};
    printf("%s\n", match_parens(lst).c_str());
    return 0;
}

//C++/MatchParens/