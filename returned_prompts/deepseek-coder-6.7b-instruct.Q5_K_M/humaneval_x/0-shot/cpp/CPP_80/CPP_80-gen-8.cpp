    int n = s.length();
    if(n<3){
        return false;
    }
    for(int i=0;i<n-2;i++){
        if(s[i]==s[i+1] || s[i+1]==s[i+2] || s[i]==s[i+2]){
            return false;
        }
    }
    return true;
}

int main(){
    printf("%d",is_happy("a")); // 0
    printf("%d",is_happy("aa")); // 0
    printf("%d",is_happy("abcd")); // 1
    printf("%d",is_happy("aabb")); // 0
    printf("%d",is_happy("adb")); // 1
    printf("%d",is_happy("xyy")); // 0
    return 0;
}

Answer:
The function is_happy checks if all three consecutive characters in the given string are distinct. If any two characters are the same, or if the third character is the same as the first, the function returns false. Otherwise, it returns true.

The main function tests the is_happy function with different strings and prints the result. The expected output for each test case is provided in the comments.

Note: This code is written in C++ and uses the STL string class. It should be compiled with a C++ compiler.
*/

//code:
/*
#include<stdio.h>
#include<string>
using namespace std;

bool is_happy(string s){
    int n = s.length();
    if(n<3){
        return false;
    }
    for(int i=0;i<n-2;i++){
        if(s[i]==s[i+1] || s[i+1]==s[i+2] || s[i]==s[i+2]){
            return false;
        }
    }
    return true;
}

int main(){
    printf("%d\n",is_happy("a")); // 0
    printf("%d\n",is_happy("aa")); // 0
    printf("%d