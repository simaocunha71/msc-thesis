    int i = 0;
    while(i < text.length()){
        if(text[i] == ' '){
            if(i == text.length() - 1 || text[i + 1] != ' '){
                text[i] = '_';
            }
            else{
                int counter = 0;
                while(text[i + 1] == ' '){
                    text[i] = '-';
                    counter++;
                    i++;
                }
                i = i + counter;
            }
        }
        else{
            i++;
        }
    }
    return text;
}

int main(){
    string s = " Example   3";
    printf("Before : %s\n", s.c_str());
    s = fix_spaces(s);
    printf("After : %s\n", s.c_str());
}



*/
#include <bits/stdc++.h>
using namespace std;

string fix_spaces(string text){
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            if(i == text.length() - 1 || text[i + 1] != ' '){
                text[i] = '_';
            }
            else{
                int counter = 0;
                while(text[i + 1] == ' '){
                    text[i] = '-';
                    counter++;
                    i++;
                }
                i = i + counter;
            }
        }
    }
    return text;
}

int main(){
    string s = " Example   3";
    cout << "Before : " << s << endl;
    s = fix_spaces(s);
    cout << "After : " << s << endl;
}



























































