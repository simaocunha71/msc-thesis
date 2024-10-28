    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            count++;
        } else if(brackets[i] == '>'){
            if(count == 0){
                return false;
            }
            count--;
        }
    }

    if(count != 0){
        return false;
    }

    return true;
}

int main(){
    printf(correct_bracketing("<") ? "true" : "false");
    printf(correct_bracketing("<>") ? "true" : "false");
    printf(correct_bracketing("<<><>>") ? "true" : "false");
    printf(correct_bracketing("><<>") ? "true" : "false");
    return 0;
}

*/

#include<iostream>
#include<string>
using namespace std;

bool correct_bracketing(string brackets){
    int count = 0;
    for(int i = 0; i < brackets.length(); i++){
        if(brackets[i] == '<'){
            count++;
        } else if(brackets[i] == '>'){
            if(count == 0){
                return false;
            }
            count--;
        }
    }
    return count == 0;
}

int main(){
    cout << (correct_bracketing("<") ? "true" : "false") << endl;
    cout << (correct_bracketing("<>") ? "true" : "false") << endl;
    cout << (correct_bracketing("<<><>>") ? "true" : "false") << endl;
    cout << (correct_bracketing("><<>") ? "true" : "false") << endl;
    return 0;
}

//test
/*
.>.<.
..><..
.<<><>>.
.><<>.
*/

//answer
/*
false
true
true
false
*/

// The function correct_brack