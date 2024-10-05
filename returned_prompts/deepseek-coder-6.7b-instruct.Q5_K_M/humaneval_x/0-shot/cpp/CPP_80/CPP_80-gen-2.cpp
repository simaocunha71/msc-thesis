    if(s.length() < 3){
        return false;
    }
    for(int i = 0; i < s.length()-2; i++){
        if(s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2]){
            return false;
        }
    }
    return true;
}

int main(){
    printf("%d",is_happy("adb"));
    return 0;
}
*/

// Code Ends


// Code Starts
#include <stdio.h>
#include <string.h>

int is_happy(char *s) {
    int n = strlen(s);
    if(n < 3) {
        return 0;
    }
    for(int i = 0; i < n-2; i++) {
        if(s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    printf("%d", is_happy("adb"));
    return 0;
}
// Code Ends

/*
Note:
In C++, you can use the <string> library to work with strings, and return a boolean value from the function.
In C, you can use the <string.h> library to work with strings, and return an integer value from the function. 1 stands for true (happy string) and 0 for false (not happy string).
*/

// Code Starts
#include <stdio.h>
#include <string.h>

int is_happy(char *s) {
    int n = strlen(s);
    if(n < 3) {
        return 0;
    }
    for(int i = 0; i < n-2; i++) {
        if(s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+