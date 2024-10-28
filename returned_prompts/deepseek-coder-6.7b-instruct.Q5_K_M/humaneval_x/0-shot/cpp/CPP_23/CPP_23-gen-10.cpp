    int length = 0;
    for(char c : str){
        length++;
    }
    return length;
}

int main(){
    printf("%d\n", strlen(""));
    printf("%d\n", strlen("abc"));
    return 0;
}

*/

#include <iostream>
#include <string>

using namespace std;

int strlen(string str) {
    int length = 0;
    for(char c : str){
        length++;
    }
    return length;
}

int main() {
    cout << strlen("") << endl;
    cout << strlen("abc") << endl;
    return 0;
}

//test/cplusplus/string/strrev.cpp
/*
