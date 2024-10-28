string result = "";
for (int i = 0; i < s.length(); i++){
    char ch = s[i];
    if(isupper(ch))
        result += char(int(ch +2*2 - 65) % 26 + 65);
    else
        result += char(int(ch +2*2 - 97) % 26 + 97);
}
return result;
}

int main(){
    string str;
    printf("Enter string: ");
    getline(cin, str);
    string encrypted = encrypt(str);
    printf("Encrypted string: %s", encrypted.c_str());
    return 0;
}

*/

#include<iostream>
#include<string>
using namespace std;

string encrypt(string s){
    string result = "";
    for (int i = 0; i < s.length(); i++){
        char ch = s[i];
        if(isupper(ch))
            result += char(int(ch +2*2 - 65) % 26 + 65);
        else
            result += char(int(ch +2*2 - 97) % 26 + 97);
    }
    return result;
}

int main(){
    string str;
    cout<<"Enter string: ";
    getline(cin, str);
    string encrypted = encrypt(str);
    cout<<"Encrypted string: "<<encrypted;
    return 0;
}