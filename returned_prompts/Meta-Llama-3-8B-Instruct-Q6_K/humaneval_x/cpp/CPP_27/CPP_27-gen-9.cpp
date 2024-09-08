    for(int i=0; i<str.length(); i++){
        if(str[i]>='a' && str[i]<='z'){
            str[i] = str[i] - 32;
        }
        else if(str[i]>='A' && str[i]<='Z'){
            str[i] = str[i] + 32;
        }
    }
    return str;
}

int main(){
    string str;
    printf("Enter a string: ");
    getline(cin, str);
    printf("Flipped string: %s\n", filp_case(str).c_str());
    return 0;
}

Answer:
#include<iostream>
#include<string>
using namespace std;

string flip_case(string str) {
    string result = "";
    for (char ch : str) {
        if (isupper(ch))
            result += tolower(ch);
        else
            result += toupper(ch);
    }
    return result;
}

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    cout << "Flipped string: " << flip_case(str) << endl;
    return 0;
}