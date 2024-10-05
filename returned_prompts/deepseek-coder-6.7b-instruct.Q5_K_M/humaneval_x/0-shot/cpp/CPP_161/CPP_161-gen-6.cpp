    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            if(islower(s[i])){
                s[i] = toupper(s[i]);
            }
            else{
                s[i] = tolower(s[i]);
            }
        }
    }
    return s;
}
int main(){
    printf("%s", solve("1234").c_str());
    return 0;
}


A: The code you posted seems to be correct. It checks each character of the given string whether it is an alphabet or not. If it is an alphabet, then it changes its case. After the loop, it returns the modified string.
In your example, when you call solve("1234"), it will return "4321" as the string "1234" contains no letters.

A: In case you need a version that simply reverses the string if it contains no letters, you could use the following code:
#include<stdio.h>
#include<string>
using namespace std;

string solve(string s){
    bool hasLetters = false;
    for(char& c : s){
        if(isalpha(c)){
            hasLetters = true;
            c = islower(c) ? toupper(c) : tolower(c);
        }
    }
    return hasLetters ? s : string(s.rbegin(), s.rend());
}

int main(){
    printf("%s\n", solve("1234").c_str());
    printf("%s\n", solve("#a@C").c_str());
    printf("%s\n", solve("ab").c_str());
    return 0;
}

In this version, the code checks if there are any letters in the string. If there are, it changes their cases. If there are no letters, it reverses the string.

A: Here is a Python version of your code:
def solve(s):
    hasLetters = False
    sList = list(s)
    for i in range(len(s)):
        if s