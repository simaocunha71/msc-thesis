    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(i % 2 == 0 && (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')){
            count++;
        }
    }
    return count;
}

int main(){
    string s;
    printf("Enter a string: ");
    cin >> s;
    printf("Number of uppercase vowels at even indices: %d\n", count_upper(s));
    return 0;
}

B:
#include <iostream>
#include <string>
using namespace std;

int count_upper(string s){
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(i % 2 == 0 && (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')){
            count++;
        }
    }
    return count;
}

int main(){
    string s;
    cout << "Enter a string: ";
    cin >> s;
    cout << "Number of uppercase vowels at even indices: " << count_upper(s) << endl;
    return 0;
}

C:
#include <iostream>
#include <string>
using namespace std;

int count_upper(string s){
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(i % 2 == 0 && (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')){
            count++;
        }
    }
    return count;
}

int main(){
    string s;
    cout << "Enter a string: ";
    cin >> s;
    cout << "Number of uppercase vowels at even indices: " << count_upper(s) << endl;
    return 0;
}
D:
#include <iostream>
#include <string>
using namespace std;

int count_upper(string s){
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(i % 2 == 0 && (s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i