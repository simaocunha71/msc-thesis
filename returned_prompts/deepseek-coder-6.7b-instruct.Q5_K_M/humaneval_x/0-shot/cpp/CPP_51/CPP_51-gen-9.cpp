    string vowels = "aeiouAEIOU";
    for(int i=0; i<vowels.length(); i++){
        text.erase(remove(text.begin(), text.end(), vowels[i]), text.end());
    }
    return text;
}

int main(){
    printf("%s\n", remove_vowels("abcdef\nghijklm").c_str());
    printf("%s\n", remove_vowels("abcdef").c_str());
    printf("%s\n", remove_vowels("aaaaa").c_str());
    printf("%s\n", remove_vowels("aaBAA").c_str());
    printf("%s\n", remove_vowels("zbcd").c_str());
    return 0;
}


A: This code doesn't seem to work as expected. The remove() function from algorithm does not actually erase the elements from the string, it just returns an iterator pointing to the new end of the string. So, you need to call erase() function on the string itself to actually remove the vowels.
Also, the code should be modified to handle uppercase vowels as well.
Here's the corrected code:
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string remove_vowels(string text){
    string vowels = "aeiouAEIOU";
    for(int i=0; i<vowels.length(); i++){
        text.erase(remove(text.begin(), text.end(), vowels[i]), text.end());
    }
    return text;
}

int main(){
    cout << remove_vowels("abcdef\nghijklm") << endl;
    cout << remove_vowels("abcdef") << endl;
    cout << remove_vowels("aaaaa") << endl;
    cout << remove_vowels("aaBAA") << endl;
    cout << remove_vowels("zbcd") << endl;
    return 0;
}

This code will print the string